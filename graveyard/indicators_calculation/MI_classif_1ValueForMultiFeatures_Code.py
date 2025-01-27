from sklearn.utils.validation import _deprecate_positional_args, check_X_y
from sklearn.utils.multiclass import check_classification_targets
import numpy as np
from scipy.sparse import issparse
from sklearn.utils import check_random_state
# TEMPORARY
# from sklearn.utils.fixes import _astype_copy_false
from sklearn.preprocessing import scale
from sklearn.neighbors import NearestNeighbors, KDTree
from scipy.special import digamma


def _compute_mi_cd_1ValueForMultiFeatures(c, d, n_neighbors):
    """Compute mutual information between continuous (multi-dimensional) and discrete variables.
    Parameters
    ----------
    c : ndarray, shape (n_samples, n_features)
        Samples of a continuous random multi-dimensional variable.
    d : ndarray, shape (n_samples,)
        Samples of a discrete random variable.
    n_neighbors : int
        Number of nearest neighbors to search for each point, see [1]_.
    Returns
    -------
    mi : float
        Estimated mutual information. If it turned out to be negative it is
        replace by 0.

    Notes
    -----
    True mutual information can't be negative. If its estimate by a numerical
    method is negative, it means (providing the method is adequate) that the
    mutual information is close to 0 and replacing it by 0 is a reasonable
    strategy.

    References
    ----------
    .. [1] B. C. Ross "Mutual Information between Discrete and Continuous
       Data Sets". PLoS ONE 9(2), 2014.
    """

    n_samples = c.shape[0]
#    c = c.reshape((-1, 1))

    radius = np.empty(n_samples)
    label_counts = np.empty(n_samples)
    k_all = np.empty(n_samples)
    nn = NearestNeighbors()
    for label in np.unique(d):
        mask = d == label
        count = np.sum(mask)
        if count > 1:
            k = min(n_neighbors, count - 1)
            nn.set_params(n_neighbors=k)
            nn.fit(c[mask])
            r = nn.kneighbors()[0]
            radius[mask] = np.nextafter(r[:, -1], 0)
            k_all[mask] = k
        #end of if count > 1
        label_counts[mask] = count
    #end of for label in np.unique(d)

    # Ignore points with unique labels.
    mask = label_counts > 1
    n_samples = np.sum(mask)
    label_counts = label_counts[mask]
    k_all = k_all[mask]
    c = c[mask]
    radius = radius[mask]

    kd = KDTree(c)
    m_all = kd.query_radius(c, radius, count_only=True, return_distance=False)
    m_all = np.array(m_all) - 1.0

    mi = (digamma(n_samples) + np.mean(digamma(k_all)) -
          np.mean(digamma(label_counts)) -
          np.mean(digamma(m_all + 1)))

##    print("mi before max with 0 is ", mi)
    return max(0, mi)

#end of def _compute_mi_cd_1ValueForMultiFeatures(c, d, n_neighbors)


def _compute_mi_1ValueForMultiFeatures(X, y, X_discrete, y_discrete, n_neighbors=3):
    """Compute mutual information between two variables.
    This is a simple wrapper which selects a proper function to call based on
    whether `X` and `y` are discrete or not.
    """
    if X_discrete and y_discrete:
#        return mutual_info_score(X, y)
        raise ValueError("_compute_mi_1ValueForMultiFeatures: Add code for both X and y discrete!")
    elif X_discrete and not y_discrete:
#        return _compute_mi_cd(y, X, n_neighbors)
        raise ValueError("_compute_mi_1ValueForMultiFeatures: Add code for X discrete and y continuous!")
    elif not X_discrete and y_discrete:
        return _compute_mi_cd_1ValueForMultiFeatures(X, y, n_neighbors)
    else:
#        return _compute_mi_cc(X, y, n_neighbors)
        raise ValueError("_compute_mi_1ValueForMultiFeatures: Add code for both X and y continuous!")
    #end of if X_discrete and y_discrete
#end of def _compute_mi_1ValueForMultiFeatures(X, y, X_discrete, y_discrete, n_neighbors=3)


def _estimate_mi_1ValueForMultiFeatures(X, y, discrete_features='auto', 
                                        discrete_target=False, n_neighbors=3, 
                                        copy=True, random_state=None):
    """Estimate mutual information between all-features-together and the target.

    Parameters
    ----------
    X : array-like or sparse matrix, shape (n_samples, n_features)
        Feature matrix.
    y : array-like of shape (n_samples,)
        Target vector.
    discrete_features : {'auto', bool}, default='auto'
        If bool, then determines whether to consider all features discrete
        or continuous. If 'auto', it is assigned to False for dense `X` 
        and to True for sparse `X`.
    discrete_target : bool, default=False
        Whether to consider `y` as a discrete variable.
    n_neighbors : int, default=3
        Number of neighbors to use for MI estimation for continuous variables,
        see [1]_ and [2]_. Higher values reduce variance of the estimation, but
        could introduce a bias.
    copy : bool, default=True
        Whether to make a copy of the given data. If set to False, the initial
        data will be overwritten.
    random_state : int, RandomState instance or None, default=None
        Determines random number generation for adding small noise to
        continuous variables in order to remove repeated values.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    mi : ndarray, shape (1,)
        Estimated mutual information between all-features-together and the target.
        A negative value will be replaced by 0.

    References
    ----------
    .. [1] A. Kraskov, H. Stogbauer and P. Grassberger, "Estimating mutual
           information". Phys. Rev. E 69, 2004.
    .. [2] B. C. Ross "Mutual Information between Discrete and Continuous
           Data Sets". PLoS ONE 9(2), 2014.
    """

    X, y = check_X_y(X, y, accept_sparse='csc', y_numeric=not discrete_target)
    n_samples, n_features = X.shape

    if isinstance(discrete_features, (str, bool)):
        if isinstance(discrete_features, str):
            if discrete_features == 'auto':
                discrete_features = issparse(X)
            else:
                raise ValueError("Invalid string value for discrete_features.")
        discrete_mask = np.empty(n_features, dtype=bool)
        discrete_mask.fill(discrete_features)
    else:
        raise ValueError("Array option for discrete_features taken out; Features need to be all-discrete or all-continuous")
    #end of if isinstance(discrete_features, (str, bool))

    continuous_mask = ~discrete_mask
    if np.any(continuous_mask) and issparse(X):
        raise ValueError("Sparse matrix `X` can't have continuous features.")

    rng = check_random_state(random_state)
    if np.any(continuous_mask):
        if copy:
            X = X.copy()

        if not discrete_target:
            X[:, continuous_mask] = scale(X[:, continuous_mask],
                                          with_mean=False, copy=False)

        # Add small noise to continuous features as advised in Kraskov et. al.
        # TEMPORARY
        # X = X.astype(float, **_astype_copy_false(X))
        means = np.maximum(1, np.mean(np.abs(X[:, continuous_mask]), axis=0))
        X[:, continuous_mask] += 1e-10 * means * rng.randn(
                n_samples, np.sum(continuous_mask))
    #end of if np.any(continuous_mask)

    if not discrete_target:
        y = scale(y, with_mean=False)
        y += 1e-10 * np.maximum(1, np.mean(np.abs(y))) * rng.randn(n_samples)

#    mi = [_compute_mi_1ValueForMultiFeatures(X, y, discrete_mask, discrete_target, n_neighbors)]
    mi = [_compute_mi_1ValueForMultiFeatures(X, y, discrete_features, discrete_target, n_neighbors)]

    return np.array(mi)

#end of def _estimate_mi_1ValueForMultiFeatures(X, y, discrete_features='auto',....)
 

@_deprecate_positional_args
def MI_classif_1ValueForMultiFeatures(X, y, *, discrete_features='auto', n_neighbors=3,
                                      copy=True, random_state=None):
    """Estimate mutual information for all-features-together and a discrete target variable.

    Mutual information (MI) [1]_ between two random variables is a non-negative
    value, which measures the dependency between the variables. It is equal
    to zero if and only if two random variables are independent, and higher
    values mean higher dependency.

    The function relies on nonparametric methods based on entropy estimation
    from k-nearest neighbors distances as described in [2]_ and [3]_. Both
    methods are based on the idea originally proposed in [4]_.

    Parameters
    ----------
    X : array-like or sparse matrix, shape (n_samples, n_features)
        Feature matrix.
    y : array-like of shape (n_samples,)
        Target vector.
    discrete_features : {'auto', bool}, default='auto'
        If bool, then determines whether to consider all features discrete
        or continuous.  If 'auto', it is assigned to False for dense `X` 
        and to True for sparse `X`.
    n_neighbors : int, default=3
        Number of neighbors to use for MI estimation for continuous variables,
        see [2]_ and [3]_. Higher values reduce variance of the estimation, but
        could introduce a bias.
    copy : bool, default=True
        Whether to make a copy of the given data. If set to False, the initial
        data will be overwritten.
    random_state : int, RandomState instance or None, default=None
        Determines random number generation for adding small noise to
        continuous variables in order to remove repeated values.
        Pass an int for reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    mi : ndarray, shape (1,)
        Estimated mutual information between all-features-together and the target.

    Notes
    -----
    1. The term "discrete features" is used instead of naming them
       "categorical", because it describes the essence more accurately.
       For example, pixel intensities of an image are discrete features
       (but hardly categorical) and you will get better results if mark them
       as such. Also note, that treating a continuous variable as discrete and
       vice versa will usually give incorrect results, so be attentive about
       that.
    2. True mutual information can't be negative. If its estimate turns out
       to be negative, it is replaced by zero.

    References
    ----------
    .. [1] `Mutual Information
           <https://en.wikipedia.org/wiki/Mutual_information>`_
           on Wikipedia.
    .. [2] (1.,2.) A. Kraskov, H. Stogbauer and P. Grassberger, "Estimating mutual
           information". Phys. Rev. E 69, 2004.
    .. [3] (1.,2.) B. C. Ross "Mutual Information between Discrete and Continuous
           Data Sets". PLoS ONE 9(2), 2014.
    .. [4] L. F. Kozachenko, N. N. Leonenko, "Sample Estimate of the Entropy
           of a Random Vector:, Probl. Peredachi Inf., 23:2 (1987), 9-16
    """

    check_classification_targets(y)
    return _estimate_mi_1ValueForMultiFeatures(X, y, discrete_features, True, 
                                               n_neighbors, copy, random_state)
#end of def MI_classif_1ValueForMultiFeatures(X, y, *, discrete_features='auto', n_neighbors=3,...)



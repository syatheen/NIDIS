echo Doing 0 to 9
cat 1/NN_U_C_?_In113_39_F.txt | wc
echo Above should be 10
echo Doing 10 to 99
cat 1/NN_U_C_??_In113_39_F.txt | wc
echo Above should be 90
echo Doing 100 to 999
cat 1/NN_U_C_???_In113_39_F.txt | wc
echo Above should be 900
echo Doing 1000 to 9999
cat 1/NN_U_C_????_In113_39_F.txt | wc
echo Above should be 9000
echo Doing 10000 to 49999
cat 1/NN_U_C_[1-4]????_In113_39_F.txt | wc
echo Above should be 40000
echo Doing 50000 to 99999
cat 1/NN_U_C_[5-9]????_In113_39_F.txt | wc
echo Doing 100000 to 149999
cat 1/NN_U_C_1[0-4]????_In113_39_F.txt | wc
echo Doing 150000 to 199999
cat 1/NN_U_C_1[5-9]????_In113_39_F.txt | wc
echo Doing 200000 to 249999
cat 1/NN_U_C_2[0-4]????_In113_39_F.txt | wc
echo Doing 250000 to 299999
cat 1/NN_U_C_2[5-9]????_In113_39_F.txt | wc
echo Doing 300000 to 349999
cat 1/NN_U_C_3[0-4]????_In113_39_F.txt | wc
echo Doing 350000 to 399999
cat 1/NN_U_C_3[5-9]????_In113_39_F.txt | wc
echo Doing 400000 to 449999
cat 1/NN_U_C_4[0-4]????_In113_39_F.txt | wc
echo Doing 450000 to 499999
cat 1/NN_U_C_4[5-9]????_In113_39_F.txt | wc
echo Above should be 19758
echo ALL DONE


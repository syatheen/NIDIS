import os
import sys
import time
from multiprocessing import Pool, cpu_count
from CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_V2_MultiProc \
    import main as CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_V2_MultiProc_Main


def run_calc(parameters):
    # calling a different script
    # python /discover/nobackup/jacaraba/development/benchmark-amy/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_V2.py \
    # ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]} ${args[6]} ${args[7]} ${args[8]} ${args[9]} \
    # ${args[10]} >& NClcFI1X1_ClmGrd1D_V2b_ND_V2_${args[0]}${args[1]}${args[10]}${args[2]}To${args[3]}_${args[4]}${args[5]}_${args[6]}_${args[7]}_${args[8]}_${args[9]}.out
    # print(parameters)

    # ['N', 'N', '20060103', '20191231', 'USDM', 'CONUS', '113', '1', '38', '884', 'P']

    CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_V2_MultiProc_Main(
        IfMakeTargetBinary=parameters[0], # Choices are 'Y' for yes, and 'N' for no
        IfIncludeD0AsDrought=parameters[1], # Choices are 'Y' for yes, and 'N' for no
        BeginYYYYMMDD_Str=parameters[2], # Beginning YYYYMMDD, this is also a Tuesday
        EndYYYYMMDD_Str=parameters[3], # Ending YYYYMMDD, this is also a Tuesday
        TargetVariable=parameters[4], # Choices are 'USDM', 'CPC_S' (for short-term), 'CPC_LE' (for long-term Eastern), and 'CPC_LW' (for long-term Western)  
        SpatialDomain=parameters[5], # Choices are 'CONUS'
        WhichArgForNumInpLayers= 6, # Which argument has info about number of input layers, goes to 6 since its indexing
        NumInpLayers=int(round(float(parameters[6]))), #int(round(float(sys.argv[7]))), # 113 for all input channels, 0 for All CPC Blend input channels, -10 for remotely-sensed, -11 for modeled, -12 for modeled+PrecipObs, -50 for all NDMC Blend input channels
        NumInpsForNDFracMI=parameters[7],
        WhichInpCombinForNDFracMI=int(round(float(parameters[8]))), #int(round(float(sys.argv[9]))), # 0-start
        Which_1D_Pixel=int(round(float(parameters[9]))), #int(round(float(sys.argv[10]))), # Which 1D number of nClimGrid pixels # 0-start
        WhichSeason=parameters[10] # Choices are 'P' for sPring (Mar-May), 'U' for sUmmer (Jun-Aug), 'F' for Fall (Sep-Nov), 'W' for Winter (Dec-Feb), 'A' for all-seasons-together
    )

    return


def read_config(config_filename):
    """
    Read tasks[X].conf configuration file.
    """
    clean_lines = []
    file = open(config_filename, 'r')
    lines = file.readlines()
    for line in lines:
        clean_lines.append(line.strip().split(' ')[-11:])
    return clean_lines


def main():

    start_time = time.time()

    # configs to read
    init_config = int(sys.argv[1])
    end_config = int(sys.argv[2])
    task_dir = sys.argv[3]

    os.makedirs('FI1X1_ClmGrd1D_V2b_New/1/', exist_ok=True)
    os.makedirs('SSiz1X1_ClmGrd1D_V2b_New/1/', exist_ok=True)
    os.makedirs('WSiz1X1_ClmGrd1D_V2b_New/1/', exist_ok=True)

    print(init_config, end_config)

    # read configuration files
    all_parameters = []
    for config_id in range(init_config, end_config):

        single_config_parameters = read_config(
            os.path.join(
                task_dir,
                f'tasks{config_id}.conf'
            )
        )
        all_parameters.extend(single_config_parameters)


    # multiprocessing queue
    p = Pool(processes=90)
    p.starmap(
        run_calc,
        zip(all_parameters)
    )

    print("End time: ", time.time() - start_time)

    return

if __name__ == "__main__":
    main()

import os

# os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyradiomics')
# os.system('pip install pyradiomics')
try:
    import radiomics
    from radiomics import featureextractor
except:
    os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyradiomics')
    import radiomics
    from radiomics import featureextractor

import pandas as pd

if __name__ == '__main__':
    extractor = featureextractor.RadiomicsFeatureExtractor()

    extractor.enableAllFeatures()
    extractor.enableAllImageTypes()
    extractor.enabledFeatures['glcm'] = ['Autocorrelation',
                                         'JointAverage',
                                         'ClusterProminence',
                                         'ClusterShade',
                                         'ClusterTendency',
                                         'Contrast',
                                         'Correlation',
                                         'DifferenceAverage',
                                         'DifferenceEntropy',
                                         'DifferenceVariance',
                                         'JointEnergy',
                                         'JointEntropy',
                                         'Imc1',
                                         'Imc2',
                                         'Idm',
                                         'MCC',
                                         'Idmn',
                                         'Id',
                                         'Idn',
                                         'InverseVariance',
                                         'MaximumProbability',
                                         'SumEntropy',
                                         'SumSquares']

    image_dir = 'C:\\Users\\maliang\\Desktop\\workspace\\nnUNet-master\\nnUNetFrame\DATASET\\nnUNet_raw\\Dataset004_Brain\\imagesTs'
    mask_dir = 'C:\\Users\\maliang\\Desktop\\workspace\\output'
    mydict = {}

    df_all = pd.DataFrame()
    for lab in [1, 2]:  # 自己把label 補上
        df = pd.DataFrame()
        patient_list = os.listdir(image_dir)
        print('patient_list', patient_list)
        for patient in patient_list:
            jpgpath = os.path.join(image_dir, patient)  # .replace('_0000', '')
            maskpath = os.path.join(mask_dir, patient).replace('_0000', '')

            print('jpgpath', jpgpath)
            print('maskpath', maskpath)
            result = extractor.execute(jpgpath, maskpath, label=lab)
            df_add = pd.DataFrame.from_dict(result.values()).T
            df_add.columns = result.keys()
            df = pd.concat((df, df_add))

        rename_dict = {col: '{}_'.format(lab) + col for col in df.columns}
        df2 = df.rename(columns=rename_dict)
        df_all = pd.concat((df_all, df2), axis=1)
    df_all.to_csv('./feature_file_all.csv')

import os
try:
    import SimpleITK as sitk
except:
    os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple SimpleITK --user')
    import SimpleITK as sitk
try:
    import pydicom
except:
    os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pydicom --user')
try:
    import nibabel
except:
    os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple nibabel --user')
try:
    import dicom2nifti
except:
    os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple dicom2nifti --user')


def dicom2Nii(folderPath, savefolder):
    count_study = 0
    for every_study in os.listdir(folderPath):  # 遍历所有的病历号
        count_study += 1
        print('every_study', every_study)
        tmp_MR_path = os.path.join(folderPath, every_study)  # DWI ,T2等
        print('tmp_MR_path', tmp_MR_path)
        for every_MRI in os.listdir(tmp_MR_path):  # 每个病历号下面可能有多次MRI
            print('every_MRI', every_MRI)
            tmp_MRI_path2 = os.path.join(tmp_MR_path, every_MRI, 'Recon2_3')
            print('tmp_MRI_path2', tmp_MRI_path2)
            all_Series_path = os.listdir(tmp_MRI_path2)
            print('all_Series_path', all_Series_path)
            for file_name in all_Series_path:
                if '.0.' in file_name:
                    os.rename(os.path.join(tmp_MR_path, every_MRI, 'Recon2_3', file_name),
                              os.path.join(tmp_MR_path, every_MRI, 'Recon2_3', file_name.replace('.0.', '.')))

            def dcm2nii(path_read, path_save):  # from CSDN;function: transfer dcm_series into nii file
                # GetGDCMSeriesIDs读取序列号相同的dcm文件
                series_id = sitk.ImageSeriesReader.GetGDCMSeriesIDs(path_read)
                # GetGDCMSeriesFileNames读取序列号相同dcm文件的路径，series[0]代表第一个序列号对应的文件
                series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(path_read, series_id[0])
                series_reader = sitk.ImageSeriesReader()
                series_reader.SetFileNames(series_file_names)
                image3d = series_reader.Execute()
                sitk.WriteImage(image3d, path_save)

            path_save = savefolder + "/" + every_study + '_' + every_MRI + ".nii.gz"
            if os.path.exists(path_save):
                continue
            dcm2nii(tmp_MRI_path2, path_save)  # 调用函数执行


if __name__ == '__main__':

    # # test
    # folderPath = r"./classfication/淮安正常人CT/normal"
    # savefolder = r"./Task019_Brain/imagesTsH"
    # dicom2Nii(folderPath, savefolder)
    # #
    folderPath = r"./classfication/江苏省人民医院嗜酸非嗜酸数据/eo"
    savefolder = r"./Task019_Brain/imagesTs"
    dicom2Nii(folderPath, savefolder)
    #
    folderPath = r"./classfication/江苏省人民医院嗜酸非嗜酸数据/un-eo"
    savefolder = r"./Task019_Brain/imagesTs"
    dicom2Nii(folderPath, savefolder)

    folderPath = r"./classfication/武大人民嗜酸和非嗜酸鼻窦炎CT/eo"
    savefolder = r"./Task019_Brain/imagesTs"
    dicom2Nii(folderPath, savefolder)
    #
    folderPath = r"./classfication/武大人民嗜酸和非嗜酸鼻窦炎CT/un-eo"
    savefolder = r"./Task019_Brain/imagesTs"
    dicom2Nii(folderPath, savefolder)

    # folderPath = r"./classfication/淮安正常人CT/normal"
    # savefolder = r"./Task019_Brain/imagesTs"
    # dicom2Nii(folderPath, savefolder)
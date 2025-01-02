import os
# edited by NickYu 2020.10.23
import numpy as np

# os.system('pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pydicom --user')

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

import shutil
import time

def dicom2Nii(folderPath, savefolder):
    count_study = 0
    for every_study in os.listdir(folderPath):  # 遍历所有的病历号
        count_study += 1
        print('every_study', every_study)
        tmp_MR_path = os.path.join(folderPath, every_study)  # DWI ,T2等
        print('tmp_MR_path', tmp_MR_path)
        for every_MRI in os.listdir(tmp_MR_path):  # 每个病历号下面可能有多次MRI
            print('every_MRI', every_MRI)
            tmp_MRI_path2 = os.path.join(tmp_MR_path, every_MRI)
            print('tmp_MRI_path2', tmp_MRI_path2)
            destination = r"./Task019_Brain/labelsTr/"
            source = os.path.join(tmp_MRI_path2, 'Untitled.nii.gz')
            shutil.copy(source, destination)

            time.sleep(2)
            os.rename(os.path.join(destination, 'Untitled.nii.gz'),
                      os.path.join(destination, every_study + '_' + every_MRI + '.nii.gz'))


if __name__ == "__main__":
    ##train
    folderPath = r"./data"
    savefolder = r"./Task019_Brain/labelsTr"
    dicom2Nii(folderPath, savefolder)

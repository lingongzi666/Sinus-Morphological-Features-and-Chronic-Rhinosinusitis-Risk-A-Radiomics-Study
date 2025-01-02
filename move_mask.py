import os
import shutil

if __name__ == '__main__':
    folderPath = './data'
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
            # destination = r"./Task019_Brain/labelsTr/"
            destination = os.path.join(tmp_MR_path, every_MRI)
            source = os.path.join(tmp_MRI_path2, 'Untitled.nii.gz')
            shutil.move(source, destination)
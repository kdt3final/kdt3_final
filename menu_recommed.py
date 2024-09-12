import random
import os

def menu_recommendation(sex_result, age_result, emotion_result):
    '''
    성별 분류모델 결과(str), 나이 분류모델 결과(int)), 감정 분류모델 결과(int)를 입력으로 받아서,
    추천 메뉴 3가지를 (리스트) 반환하는 함수
    경로를 알맞게 수정하고 사용할 것
    '''
    # 경로 바꿔서 사용할 것
    bev_dir = r'E:\project\kiosk\image\bev'
    cof_dir = r'E:\project\kiosk\image\cof'
    tea_dir = r'E:\project\kiosk\image\tea'

    bev_images = os.listdir(bev_dir)
    cof_images = os.listdir(cof_dir)
    tea_images = os.listdir(tea_dir)

    menu_recommendations = {
        ('M', 0, 2): [bev_images[0], cof_images[0], tea_images[0]],
        ('M', 0, 0): [bev_images[1], cof_images[1], tea_images[1]],
        ('M', 0, 1): [bev_images[2], cof_images[2], tea_images[2]],
        ('M', 1, 2): [bev_images[3], cof_images[3], tea_images[3]],
        ('M', 1, 0): [bev_images[4], cof_images[4], tea_images[4]],
        ('M', 1, 1): [bev_images[0], cof_images[0], tea_images[0]],
        ('M', 2, 2): [bev_images[1], cof_images[1], tea_images[1]],
        ('M', 2, 0): [bev_images[2], cof_images[2], tea_images[2]],
        ('M', 2, 1): [bev_images[3], cof_images[3], tea_images[3]],
        ('F', 0, 2): [bev_images[4], cof_images[4], tea_images[4]],
        ('F', 0, 0): [bev_images[0], cof_images[0], tea_images[0]],
        ('F', 0, 1): [bev_images[1], cof_images[1], tea_images[1]],
        ('F', 1, 2): [bev_images[2], cof_images[2], tea_images[2]],
        ('F', 1, 0): [bev_images[3], cof_images[3], tea_images[3]],
        ('F', 1, 1): [bev_images[4], cof_images[4], tea_images[4]],
        ('F', 2, 2): [bev_images[0], cof_images[0], tea_images[0]],
        ('F', 2, 0): [bev_images[1], cof_images[1], tea_images[1]],
        ('F', 2, 1): [bev_images[2], cof_images[2], tea_images[2]],
    }

    model_output = (sex_result, age_result, emotion_result)
    recommendation = menu_recommendations[model_output]

    return recommendation
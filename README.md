# easy_ML
"""
How can I do machine learning easily?
"""


머신러닝을 어떻게 하면 쉽게 배울 수 있고, 어떻게 코딩을 통하지 않고도 일반인들이 머신러닝을 쉽게 받아들일 수 있을까.?
이러한 생각을 통해 나온 것이 autoML이라는 친구가 있다 이 친구는 머신러닝을 알지 못하더라도 편리하게 머신러닝을 처리해주는 프로그램이다.
우린 이러한 것에 국한되지 않기 위해 머신러닝을 손쉽게 배우고 익히는 방법을 모색해보았다.
머신러닝이란, 기본적인 이론 & 수학 & 코딩이 뒷바침되어야 한다. 우린 코딩을 잘 하지 못하고 수학적인 부분에 부족함이 있는 일반인들도
손쉽게 머신러닝을 할 수 있도록 python, web을 사용하여 교육용 혹은 머신러닝기술활용 할 수 있는 프로그램은 고안중이다.



# Day-1. 머신러닝 기법을 다시 돌아보며 머신러닝의 기본 구동 순서 및 구동 원리에 대해 다시 되짚어 보았다.

## 1.Data load
## 2.find lost value
## 3.scaling
## 4.model.fit
## 5.model performance measure

# Day-2. 코딩 시작

기본적인 프로토 타입은 코딩을 완료하였다. 하지만 한파일에 모든 것을 담아 놓으니 추후에 수정하기도 힘들어 보였고 '객체지향'이라곤 찾아 볼 수 없었다.
module & package를 다시 되짚어 보며 새로운 코딩 방법을 생각해 보았다.

#Day-3. 패키지 형식의 코딩

패키지 형식으로 코딩을 시작했다.
project
┖ load_preprocess
    ┖ load.py
      preprocess.py
  model_select
    ┖ classific.py
      regression.py
      Ensemble.py
      select.py
  predicts
    ┖ predict.py
  main.py
  

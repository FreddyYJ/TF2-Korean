# TF2-Korean
## 한국어/Korean
There's english ReadMe under the Korean one.

### 소개
이 Project/Repository는 Transport Fever 2의 한글 번역을 위한 것입니다.
이 프로젝트는 GNU LGPL v3.0을 따르고 있으며, 영어 원문 혹은 한글 번역본을 참고하시면 됩니다.

이 프로젝트는 최종적으로 '모드'의 형식으로, Steam Workshop에서 배포하는 것을 목표로 하고 있습니다.

### 사용 방법
* 현재에는 이 방법을 사용하고 있으나, 최종적으로는 '모드'의 형식과 Steam Workshop을 목표로 하고 있습니다.
1. ```git clone https://github.com/FreddyYJ/TF2-Korean.git```을 실행한다.
2. ```<현재 디렉터리>/TF2-Korean```에 들어간다.
3. ```fonts```를 ```<스팀 설치 디렉터리>/stramapps/common/Transport Fever 2/res```로 복사한다.
4. ```ko```를 ```<스팀 설치 디렉터리>/stramapps/common/Transport Fever 2/res/strings```로 복사한다.
5. 게임을 실행하고 설정에서 언어를 Korean으로 바꾼다.
* 일반적으로 <스팀 설치 디렉터리>의 경우
Windows는 ```C:\Program files(x86)\Steam``` 혹은 ```D:\SteamLibrary```이고,
Linux는 ```~/.steam/steam```입니다.
게임 설치시 다른 경로를 설정하였다면 그 경로에 있을 것입니다.

### 번역 개선
개인적인 수단(이메일 등)으로 번역 개선 요청은 받지 않습니다.
개선하거나 바꾸고 싶은 번역이 있다면, 아래 방법으로 해주시기 바랍니다.
#### 환경 구축
1. ```git clone https://github.com/FreddyYJ/TF2-Korean.git```을 실행한다.
2. ```git branch <이름>```을 실행한다. 이때, <이름>은 영어를 사용하여 아무거나 해주시면 된다.(한국어, -/_ 외 특수문자, 띄어쓰기 금지)
3. ```git checkout <이름>```을 실행한다.
4. ```git push -u origin <이름>```을 실행한다.
5. Poedit을 설치한다. 공식 홈페이지: https://poedit.net/download
#### 번역
1. ```<현재 디렉터리>/TF2-Korean/ko/LC_MESSAGES/base.po```와 ```<현재 디렉터리>/TF2-Korean/ko/LC_MESSAGES/res.po```을 Poedit으로 열어 수정한다.
2. 저장하고 Poedit을 닫는다.
3. ```<현재 디렉터리>```로 돌아온다.
4. ```git add *```을 실행한다.
5. ```git commit -m "<커밋 제목>"```을 실행한다. <커밋 제목>은 아무거나 가능하지만, 영어만 사용하기를 권장한다. 띄어쓰기를 포함할 수 있다.
6. ```git push```를 실행한다.
7. 1~6을 반복한다.
#### 반영 요청
번역을 하는게 끝이 아니고, 번역한 것을 실제로 반영할 수 있도록 '요청'해야 합니다.
1. 현재 Github페이지로 접속한다.
2. 상단의 Pull Requests를 누른다.
3. 초록색 버튼 New Pull Request를 누른다.
4. base를 master로, compare를 <이름>으로 설정한다.
5. 잠시 기다린 후 초록색 버튼 Create Pull Request를 누른다.
여기까지 하면 제가 보고, 반영할지 판단하여 반영할 것입니다.

## 영어/English

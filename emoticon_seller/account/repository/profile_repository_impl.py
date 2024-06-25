from account.entity.profile import Profile
from account.repository.profile_repository import ProfileRepository


class ProfileRepositoryImpl(ProfileRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def findByEmail(self, email):
        try:
            profile = Profile.objects.get(email=email)
            return profile
        except Profile.DoesNotExist:
            print(f"email로 계정 정보를 찾을 수 없습니다: {email}")
            return None
        except Exception as e:
            print(f'email 중복 검사 중 에러: {e}')
            return None

    def findByNickname(self, nickname):
        try:
            profile = Profile.objects.get(nickname=nickname)
            return profile
        except Profile.DoesNotExist:
            print('닉네임과 일치하는 계정이 없습니다')
            return None
        except Exception as e:
            print(f"닉네임 중복 검사 중 오류 발생: {e}")
            return None

    def create(self, nickname, email, account):
        profile = Profile.objects.create(nickname=nickname, email=email,account=account)
        return profile






from main.utils.VerifyCode import EmailKeyGen, TOTP
from main.Config.GlobalConfig import EMAIL_CODE_LENGTH, ENCRYP_KEY, ADMIN_CODE_LENGTH
# ------------
# 待解决

EMAIL_CODE = EmailKeyGen(EMAIL_CODE_LENGTH)
EMAIL_CODE.start()
ADMIN_CODE = TOTP(ENCRYP_KEY, ADMIN_CODE_LENGTH)
ADMIN_CODE.start()

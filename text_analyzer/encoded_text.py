import base64



bad_list = base64.b64decode("R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsT\
mFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2Njd\
XBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT").decode().lower().split(",")

less_bad_list = base64.b64decode("RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYW\
xlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ==").decode().lower().split(",")

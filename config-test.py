# *_*coding:utf-8 *_*
import os
import sys
import socket


############ For LINUX ##############
DATA_DIR = {
	'Track1_English_Annotation': r'/home/zongtianyu/data/wangyuanxiang/xyy/ChallengeData/Track1/English/Annotation',
	'Track1_English_NoAnnotation': r'/home/zongtianyu/data/wangyuanxiang/xyy/ChallengeData/Track1/English/NoAnnotation',
	'Track1_Mandarin_Annotation': r'/home/zongtianyu/data/wangyuanxiang/xyy/ChallengeData/Track1/Mandarin/Annotation',
	'Track1_Mandarin_NoAnnotation': r'/home/zongtianyu/data/wangyuanxiang/xyy/ChallengeData/Track1/Mandarin/NoAnnotation',
	'Track2_English': r'/home/zongtianyu/data/wangyuanxiang/xyy/ChallengeData/Track2/English',
	'Track2_Mandarin': r'/home/zongtianyu/data/wangyuanxiang/xyy/ChallengeData/Track2/Mandarin',
}

PATH_TO_RAW_AUDIO = {
	'Track1_English_Annotation': os.path.join(DATA_DIR['Track1_English_Annotation'], 'Audios'),
	'Track1_English_NoAnnotation': os.path.join(DATA_DIR['Track1_English_NoAnnotation'], 'Audios'),
	'Track1_Mandarin_Annotation': os.path.join(DATA_DIR['Track1_Mandarin_Annotation'], 'Audios'),
	'Track1_Mandarin_NoAnnotation': os.path.join(DATA_DIR['Track1_Mandarin_NoAnnotation'], 'Audios'),
	'Track2_English': os.path.join(DATA_DIR['Track2_English'], 'Audios'),
	'Track2_Mandarin': os.path.join(DATA_DIR['Track2_Mandarin'], 'Audios'),
}

PATH_TO_RAW_FACE = {
	'Track1_English_Annotation': os.path.join(DATA_DIR['Track1_English_Annotation'], 'openface_face'),
	'Track1_English_NoAnnotation': os.path.join(DATA_DIR['Track1_English_NoAnnotation'], 'openface_face'),
	'Track1_Mandarin_Annotation': os.path.join(DATA_DIR['Track1_Mandarin_Annotation'], 'openface_face'),
	'Track1_Mandarin_NoAnnotation': os.path.join(DATA_DIR['Track1_Mandarin_NoAnnotation'], 'openface_face'),
	'Track2_English': os.path.join(DATA_DIR['Track2_English'], 'openface_face'),
	'Track2_Mandarin': os.path.join(DATA_DIR['Track2_Mandarin'], 'openface_face'),
}

PATH_TO_TRANSCRIPTIONS = {
	# 'Track1_English_Annotation': os.path.join(DATA_DIR['Track1_English_Annotation'], 'transcription.csv'),
	# 'Track1_English_NoAnnotation': os.path.join(DATA_DIR['Track1_English_NoAnnotation'], 'transcription.csv'),
	# 'Track1_Mandarin_Annotation': os.path.join(DATA_DIR['Track1_Mandarin_Annotation'], 'transcription.csv'),
	# 'Track1_Mandarin_NoAnnotation': os.path.join(DATA_DIR['Track1_Mandarin_NoAnnotation'], 'transcription.csv'),
	'Track2_English': os.path.join(DATA_DIR['Track2_English'], 'transcription.csv'),
	'Track2_Mandarin': os.path.join(DATA_DIR['Track2_Mandarin'], 'transcription.csv'),
}
PATH_TO_FEATURES = {
	'Track1_English_Annotation': os.path.join(DATA_DIR['Track1_English_Annotation'], 'features'),
	'Track1_English_NoAnnotation': os.path.join(DATA_DIR['Track1_English_NoAnnotation'], 'features'),
	'Track1_Mandarin_Annotation': os.path.join(DATA_DIR['Track1_Mandarin_Annotation'], 'features'),
	'Track1_Mandarin_NoAnnotation': os.path.join(DATA_DIR['Track1_Mandarin_NoAnnotation'], 'features'),
	'Track2_English': os.path.join(DATA_DIR['Track2_English'], 'features'),
	'Track2_Mandarin': os.path.join(DATA_DIR['Track2_Mandarin'], 'features'),
}


PATH_TO_PRETRAINED_MODELS = r'/home/zongtianyu/data/wangyuanxiang/xyy/baseline_model'
PATH_TO_OPENSMILE = os.path.join(PATH_TO_PRETRAINED_MODELS, r'opensmile-2.3.0')
PATH_TO_FFMPEG = os.path.join(PATH_TO_PRETRAINED_MODELS, r'ffmpeg-4.4.1-i686-static', r'ffmpeg')
PATH_TO_NOISE = os.path.join(PATH_TO_PRETRAINED_MODELS, r'musan', r'audio-select')

SAVED_ROOT = os.path.join('./saved')
DATA_DIR = os.path.join(SAVED_ROOT, 'data')
MODEL_DIR = os.path.join(SAVED_ROOT, 'model')
LOG_DIR = os.path.join(SAVED_ROOT, 'log')
PREDICTION_DIR = os.path.join(SAVED_ROOT, 'prediction')
FUSION_DIR = os.path.join(SAVED_ROOT, 'fusion')
SUBMISSION_DIR = os.path.join(SAVED_ROOT, 'submission')

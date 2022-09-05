# Copyright (c) Alibaba, Inc. and its affiliates.

from modelscope.utils.constant import Tasks


class OutputKeys(object):
    LOSS = 'loss'
    LOGITS = 'logits'
    SCORES = 'scores'
    SCORE = 'score'
    LABEL = 'label'
    LABELS = 'labels'
    INPUT_IDS = 'input_ids'
    LABEL_POS = 'label_pos'
    POSES = 'poses'
    CAPTION = 'caption'
    BOXES = 'boxes'
    KEYPOINTS = 'keypoints'
    MASKS = 'masks'
    TEXT = 'text'
    POLYGONS = 'polygons'
    OUTPUT = 'output'
    OUTPUT_IMG = 'output_img'
    OUTPUT_PCM = 'output_pcm'
    IMG_EMBEDDING = 'img_embedding'
    SPO_LIST = 'spo_list'
    TEXT_EMBEDDING = 'text_embedding'
    TRANSLATION = 'translation'
    RESPONSE = 'response'
    PREDICTION = 'prediction'
    PREDICTIONS = 'predictions'
    PROBABILITIES = 'probabilities'
    DIALOG_STATES = 'dialog_states'
    VIDEO_EMBEDDING = 'video_embedding'
    UUID = 'uuid'
    WORD = 'word'
    KWS_LIST = 'kws_list'
    TIMESTAMPS = 'timestamps'
    SPLIT_VIDEO_NUM = 'split_video_num'
    SPLIT_META_DICT = 'split_meta_dict'


TASK_OUTPUTS = {

    # ============ vision tasks ===================

    # ocr detection result for single sample
    # {
    #   "polygons": np.array with shape [num_text, 8], each polygon is
    #       [x1, y1, x2, y2, x3, y3, x4, y4]
    # }
    Tasks.ocr_detection: [OutputKeys.POLYGONS],

    # ocr recognition result for single sample
    # {
    #    "text": "电子元器件提供BOM配单"
    # }
    Tasks.ocr_recognition: [OutputKeys.TEXT],

    # face 2d keypoint result for single sample
    #   {
    #       "keypoints": [
    #           [x1, y1]*106
    #       ],
    #       "poses": [pitch, roll, yaw]
    #   }
    Tasks.face_2d_keypoints: [OutputKeys.KEYPOINTS, OutputKeys.POSES],

    # face detection result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "boxes": [
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #       ],
    #       "keypoints": [
    #           [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5],
    #           [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5],
    #           [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5],
    #           [x1, y1, x2, y2, x3, y3, x4, y4, x5, y5],
    #       ],
    #   }
    Tasks.face_detection:
    [OutputKeys.SCORES, OutputKeys.BOXES, OutputKeys.KEYPOINTS],

    # facial expression recognition result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.02, 0.02, 0.02, 0.02, 0.02],
    #       "labels": ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    #   }
    Tasks.facial_expression_recognition:
    [OutputKeys.SCORES, OutputKeys.LABELS],

    # face recognition result for single sample
    #   {
    #       "img_embedding": np.array with shape [1, D],
    #   }
    Tasks.face_recognition: [OutputKeys.IMG_EMBEDDING],

    # human detection result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "labels": ["person", "person", "person", "person"],
    #       "boxes": [
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #       ],
    #   }
    #
    Tasks.human_detection:
    [OutputKeys.SCORES, OutputKeys.LABELS, OutputKeys.BOXES],

    # face generation result for single sample
    # {
    #   "output_img": np.array with shape(h, w, 3)
    # }
    Tasks.face_image_generation: [OutputKeys.OUTPUT_IMG],

    # image classification result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "labels": ["dog", "horse", "cow", "cat"],
    #   }
    Tasks.image_classification: [OutputKeys.SCORES, OutputKeys.LABELS],

    # object detection result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "labels": ["dog", "horse", "cow", "cat"],
    #       "boxes": [
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #       ],
    #   }
    Tasks.image_object_detection:
    [OutputKeys.SCORES, OutputKeys.LABELS, OutputKeys.BOXES],

    # instance segmentation result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05],
    #       "labels": ["dog", "horse", "cow", "cat"],
    #       "masks": [
    #           np.array # 2D array containing only 0, 1
    #       ]
    #   }
    Tasks.image_segmentation:
    [OutputKeys.SCORES, OutputKeys.LABELS, OutputKeys.MASKS],

    # image matting result for single sample
    # {
    #   "output_img": np.array with shape(h, w, 4)
    #                 for matting or (h, w, 3) for general purpose
    #                 , shape(h, w) for crowd counting
    # }
    Tasks.portrait_matting: [OutputKeys.OUTPUT_IMG],

    # image editing task result for a single image
    # {"output_img": np.array with shape (h, w, 3)}
    Tasks.skin_retouching: [OutputKeys.OUTPUT_IMG],
    Tasks.image_super_resolution: [OutputKeys.OUTPUT_IMG],
    Tasks.image_colorization: [OutputKeys.OUTPUT_IMG],
    Tasks.image_color_enhancement: [OutputKeys.OUTPUT_IMG],
    Tasks.image_denoising: [OutputKeys.OUTPUT_IMG],
    Tasks.image_portrait_enhancement: [OutputKeys.OUTPUT_IMG],
    Tasks.crowd_counting: [OutputKeys.SCORES, OutputKeys.OUTPUT_IMG],

    # image generation task result for a single image
    # {"output_img": np.array with shape (h, w, 3)}
    Tasks.image_to_image_generation: [OutputKeys.OUTPUT_IMG],
    Tasks.image_to_image_translation: [OutputKeys.OUTPUT_IMG],
    Tasks.image_style_transfer: [OutputKeys.OUTPUT_IMG],
    Tasks.image_portrait_stylization: [OutputKeys.OUTPUT_IMG],

    # live category recognition result for single video
    # {
    #       "scores": [0.885272, 0.014790631, 0.014558001]
    #       "labels": ['女装/女士精品>>棉衣/棉服', '女装/女士精品>>牛仔裤', '女装/女士精品>>裤子>>休闲裤'],
    # }
    Tasks.live_category: [OutputKeys.SCORES, OutputKeys.LABELS],

    # action recognition result for single video
    # {
    #   "output_label": "abseiling"
    # }
    Tasks.action_recognition: [OutputKeys.LABELS],

    # human body keypoints detection result for single sample
    # {
    #   "poses": [
    #               [[x, y]*15],
    #               [[x, y]*15],
    #               [[x, y]*15]
    #             ]
    #   "scores": [
    #               [[score]*15],
    #               [[score]*15],
    #               [[score]*15]
    #              ]
    #   "boxes": [
    #               [[x1, y1], [x2, y2]],
    #               [[x1, y1], [x2, y2]],
    #               [[x1, y1], [x2, y2]],
    #             ]
    # }
    Tasks.body_2d_keypoints:
    [OutputKeys.POSES, OutputKeys.SCORES, OutputKeys.BOXES],

    # 3D human body keypoints detection result for single sample
    # {
    #   "poses": [
    #               [[x, y, z]*17],
    #               [[x, y, z]*17],
    #               [[x, y, z]*17]
    #             ]
    # }
    Tasks.body_3d_keypoints: [OutputKeys.POSES],

    # 2D hand keypoints result for single sample
    # {
    #     "keypoints": [
    #                     [[x, y, score] * 21],
    #                     [[x, y, score] * 21],
    #                     [[x, y, score] * 21],
    #                  ],
    #     "boxes": [
    #                 [x1, y1, x2, y2],
    #                 [x1, y1, x2, y2],
    #                 [x1, y1, x2, y2],
    #             ]
    # }
    Tasks.hand_2d_keypoints: [OutputKeys.KEYPOINTS, OutputKeys.BOXES],

    # video single object tracking result for single video
    # {
    #   "boxes": [
    #               [x1, y1, x2, y2],
    #               [x1, y1, x2, y2],
    #               [x1, y1, x2, y2],
    #             ]
    # }
    Tasks.video_single_object_tracking: [OutputKeys.BOXES],

    # live category recognition result for single video
    # {
    #       "scores": [0.885272, 0.014790631, 0.014558001],
    #       'labels': ['修身型棉衣', '高腰牛仔裤', '休闲连体裤']
    # }
    Tasks.live_category: [OutputKeys.SCORES, OutputKeys.LABELS],

    # video category recognition result for single video
    # {
    #       "scores": [0.7716429233551025],
    #       "labels": ['生活>>好物推荐']
    # }
    Tasks.video_category: [OutputKeys.SCORES, OutputKeys.LABELS],

    # image embedding result for a single image
    # {
    #   "image_bedding": np.array with shape [D]
    # }
    Tasks.product_retrieval_embedding: [OutputKeys.IMG_EMBEDDING],

    # video embedding result for single video
    # {
    #   "video_embedding": np.array with shape [D],
    # }
    Tasks.video_embedding: [OutputKeys.VIDEO_EMBEDDING],

    # virtual_try_on result for a single sample
    # {
    #    "output_img": np.ndarray with shape [height, width, 3]
    # }
    Tasks.virtual_try_on: [OutputKeys.OUTPUT_IMG],
    # text driven segmentation result for single sample
    #   {
    #       "masks": [
    #           np.array # 2D array containing only 0, 255
    #       ]
    #   }
    Tasks.text_driven_segmentation: [OutputKeys.MASKS],
    # shop segmentation result for single sample
    #   {
    #       "masks": [
    #           np.array # 2D array containing only 0, 255
    #       ]
    #   }
    Tasks.shop_segmentation: [OutputKeys.MASKS],
    # movide scene segmentation result for a single video
    # {
    #        "split_video_num":3,
    #        "split_meta_dict":
    #        {
    #           scene_id:
    #           {
    #               "shot": [0,1,2],
    #               "frame": [start_frame, end_frame]
    #           }
    #        }
    #
    # }
    Tasks.movie_scene_segmentation:
    [OutputKeys.SPLIT_VIDEO_NUM, OutputKeys.SPLIT_META_DICT],

    # ============ nlp tasks ===================

    # text classification result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "labels": ["happy", "sad", "calm", "angry"],
    #   }
    Tasks.text_classification: [OutputKeys.SCORES, OutputKeys.LABELS],

    # sentence similarity result for single sample
    #   {
    #       "scores": 0.9
    #       "labels": "1",
    #   }
    Tasks.sentence_similarity: [OutputKeys.SCORES, OutputKeys.LABELS],

    # nli result for single sample
    #   {
    #       "labels": ["happy", "sad", "calm", "angry"],
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #   }
    Tasks.nli: [OutputKeys.SCORES, OutputKeys.LABELS],

    # sentiment classification result for single sample
    # {
    #     'scores': [0.07183828949928284, 0.9281617403030396],
    #     'labels': ['1', '0']
    # }
    Tasks.sentiment_classification: [OutputKeys.SCORES, OutputKeys.LABELS],

    # zero-shot classification result for single sample
    #   {
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    #       "labels": ["happy", "sad", "calm", "angry"],
    #   }
    Tasks.zero_shot_classification: [OutputKeys.SCORES, OutputKeys.LABELS],

    # relation extraction result for a single sample
    # {
    #     "uuid": "人生信息-1",
    #     "text": "《父老乡亲》是由是由由中国人民解放军海政文工团创作的军旅歌曲，石顺义作词，王锡仁作曲，范琳琳演唱",
    #     "spo_list": [{"subject": "石顺义", "predicate": "国籍", "object": "中国"}]
    # }
    Tasks.relation_extraction: [OutputKeys.SPO_LIST],

    # translation result for a source sentence
    #   {
    #       "translation": “北京是中国的首都”
    #   }
    Tasks.translation: [OutputKeys.TRANSLATION],

    # word segmentation result for single sample
    # {
    #   "output": "今天 天气 不错 ， 适合 出去 游玩"
    # }
    Tasks.word_segmentation: [OutputKeys.OUTPUT],

    # part-of-speech result for single sample
    # [
    #     {'word': '诸葛', 'label': 'PROPN'},
    #     {'word': '亮', 'label': 'PROPN'},
    #     {'word': '发明', 'label': 'VERB'},
    #     {'word': '八', 'label': 'NUM'},
    #     {'word': '阵', 'label': 'NOUN'},
    #     {'word': '图', 'label': 'PART'},
    #     {'word': '以', 'label': 'ADV'},
    #     {'word': '利', 'label': 'VERB'},
    #     {'word': '立营', 'label': 'VERB'},
    #     {'word': '练兵', 'label': 'VERB'},
    #     {'word': '.', 'label': 'PUNCT'}
    # ]
    # TODO @wenmeng.zwm support list of result check
    Tasks.part_of_speech: [OutputKeys.WORD, OutputKeys.LABEL],

    # named entity recognition result for single sample
    # {
    #   "output": [
    #     {"type": "LOC", "start": 2, "end": 5, "span": "温岭市"},
    #     {"type": "LOC", "start": 5, "end": 8, "span": "新河镇"}
    #   ]
    # }
    Tasks.named_entity_recognition: [OutputKeys.OUTPUT],

    # text_error_correction result for a single sample
    # {
    #    "output": "我想吃苹果"
    # }
    Tasks.text_error_correction: [OutputKeys.OUTPUT],

    # text generation result for single sample
    # {
    #   "text": "this is the text generated by a model."
    # }
    Tasks.text_generation: [OutputKeys.TEXT],

    # text feature extraction for single sample
    # {
    #   "text_embedding": np.array with shape [1, D]
    # }
    Tasks.sentence_embedding: [OutputKeys.TEXT_EMBEDDING],

    # fill mask result for single sample
    # {
    #   "text": "this is the text which masks filled by model."
    # }
    Tasks.fill_mask: [OutputKeys.TEXT],

    # (Deprecated) dialog intent prediction result for single sample
    # {'output': {'prediction': array([2.62349960e-03, 4.12110658e-03, 4.12748595e-05, 3.77560973e-05,
    #        1.08599677e-04, 1.72710388e-05, 2.95618793e-05, 1.93638436e-04,
    #        6.45841064e-05, 1.15997791e-04, 5.11605394e-05, 9.87020373e-01,
    #        2.66957268e-05, 4.72324500e-05, 9.74208378e-05, 4.18022355e-05,
    #        2.97343540e-05, 5.81317654e-05, 5.44203431e-05, 6.28319322e-05,
    #        7.34537680e-05, 6.61411541e-05, 3.62534920e-05, 8.58885178e-05,
    #        8.24327726e-05, 4.66077945e-05, 5.32869453e-05, 4.16190960e-05,
    #        5.97518992e-05, 3.92273068e-05, 3.44069012e-05, 9.92335918e-05,
    #        9.25978165e-05, 6.26462061e-05, 3.32317031e-05, 1.32061413e-03,
    #        2.01607945e-05, 3.36636294e-05, 3.99156743e-05, 5.84108493e-05,
    #        2.53432900e-05, 4.95731190e-04, 2.64443643e-05, 4.46992999e-05,
    #        2.42672231e-05, 4.75615161e-05, 2.66230145e-05, 4.00083954e-05,
    #        2.90536875e-04, 4.23891543e-05, 8.63691166e-05, 4.98188965e-05,
    #        3.47019341e-05, 4.52718523e-05, 4.20905781e-05, 5.50173208e-05,
    #        4.92360487e-05, 3.56021264e-05, 2.13957210e-05, 6.17428886e-05,
    #        1.43893281e-04, 7.32152112e-05, 2.91354867e-04, 2.46623786e-05,
    #        3.61441926e-05, 3.38475402e-05, 3.44323053e-05, 5.70138109e-05,
    #        4.31488479e-05, 4.94503947e-05, 4.30105974e-05, 1.00963116e-04,
    #        2.82062047e-05, 1.15582036e-04, 4.48261271e-05, 3.99339879e-05,
    #        7.27692823e-05], dtype=float32), 'label_pos': array([11]), 'label': 'lost_or_stolen_card'}}

    # (Deprecated) dialog modeling prediction result for single sample
    # {'output' : ['you', 'are', 'welcome', '.', 'have', 'a', 'great', 'day', '!']}

    # (Deprecated) dialog state tracking result for single sample
    # {
    #     "output":{
    #         "dialog_states": {
    #             "taxi-leaveAt": "none",
    #             "taxi-destination": "none",
    #             "taxi-departure": "none",
    #             "taxi-arriveBy": "none",
    #             "restaurant-book_people": "none",
    #             "restaurant-book_day": "none",
    #             "restaurant-book_time": "none",
    #             "restaurant-food": "none",
    #             "restaurant-pricerange": "none",
    #             "restaurant-name": "none",
    #             "restaurant-area": "none",
    #             "hotel-book_people": "none",
    #             "hotel-book_day": "none",
    #             "hotel-book_stay": "none",
    #             "hotel-name": "none",
    #             "hotel-area": "none",
    #             "hotel-parking": "none",
    #             "hotel-pricerange": "cheap",
    #             "hotel-stars": "none",
    #             "hotel-internet": "none",
    #             "hotel-type": "true",
    #             "attraction-type": "none",
    #             "attraction-name": "none",
    #             "attraction-area": "none",
    #             "train-book_people": "none",
    #             "train-leaveAt": "none",
    #             "train-destination": "none",
    #             "train-day": "none",
    #             "train-arriveBy": "none",
    #             "train-departure": "none"
    #         }
    #     }
    # }
    Tasks.task_oriented_conversation: [OutputKeys.OUTPUT],

    # conversational text-to-sql result for single sample
    # {
    #   "text": "SELECT shop.Name FROM shop."
    # }
    Tasks.conversational_text_to_sql: [OutputKeys.TEXT],

    # ============ audio tasks ===================
    # asr result for single sample
    # { "text": "每一天都要快乐喔"}
    Tasks.auto_speech_recognition: [OutputKeys.TEXT],

    # audio processed for single file in PCM format
    # {
    #   "output_pcm": pcm encoded audio bytes
    # }
    Tasks.speech_signal_process: [OutputKeys.OUTPUT_PCM],
    Tasks.acoustic_echo_cancellation: [OutputKeys.OUTPUT_PCM],
    Tasks.acoustic_noise_suppression: [OutputKeys.OUTPUT_PCM],

    # text_to_speech result for a single sample
    # {
    #    "output_pcm": {"input_label" : np.ndarray with shape [D]}
    # }
    Tasks.text_to_speech: [OutputKeys.OUTPUT_PCM],

    # {
    #     "kws_list": [
    #         {
    #             'keyword': '',        # the keyword spotted
    #             'offset': 19.4,       # the keyword start time in second
    #             'length': 0.68,       # the keyword length in second
    #             'confidence': 0.85    # the possibility if it is the keyword
    #         },
    #         ...
    #     ]
    # }
    Tasks.keyword_spotting: [OutputKeys.KWS_LIST],

    # ============ multi-modal tasks ===================

    # image caption result for single sample
    # {
    #   "caption": "this is an image caption text."
    # }
    Tasks.image_captioning: [OutputKeys.CAPTION],

    # visual grounding result for single sample
    # {
    #       "boxes": [
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #           [x1, y1, x2, y2],
    #       ],
    #       "scores": [0.9, 0.1, 0.05, 0.05]
    # }
    Tasks.visual_grounding: [OutputKeys.BOXES, OutputKeys.SCORES],

    # text_to_image result for a single sample
    # {
    #    "output_img": np.ndarray with shape [height, width, 3]
    # }
    Tasks.text_to_image_synthesis: [OutputKeys.OUTPUT_IMG],

    # text_to_speech result for a single sample
    # {
    #    "output_pcm": {"input_label" : np.ndarray with shape [D]}
    # }
    Tasks.text_to_speech: [OutputKeys.OUTPUT_PCM],

    # multi-modal embedding result for single sample
    # {
    #   "img_embedding": np.array with shape [1, D],
    #   "text_embedding": np.array with shape [1, D]
    # }
    Tasks.multi_modal_embedding:
    [OutputKeys.IMG_EMBEDDING, OutputKeys.TEXT_EMBEDDING],

    # generative multi-modal embedding result for single sample
    # {
    #   "img_embedding": np.array with shape [1, D],
    #   "text_embedding": np.array with shape [1, D],
    #   "caption": "this is an image caption text."
    # }
    Tasks.generative_multi_modal_embedding:
    [OutputKeys.IMG_EMBEDDING, OutputKeys.TEXT_EMBEDDING, OutputKeys.CAPTION],

    # multi-modal similarity result for single sample
    # {
    #   "img_embedding": np.array with shape [1, D],
    #   "text_embedding": np.array with shape [1, D],
    #   "similarity": float
    # }
    Tasks.multi_modal_similarity:
    [OutputKeys.IMG_EMBEDDING, OutputKeys.TEXT_EMBEDDING, OutputKeys.SCORES],

    # VQA result for a sample
    # {"text": "this is a text answser. "}
    Tasks.visual_question_answering: [OutputKeys.TEXT],

    # auto_speech_recognition result for a single sample
    # {
    #    "text": "每天都要快乐喔"
    # }
    Tasks.auto_speech_recognition: [OutputKeys.TEXT],

    # {
    #       "scores": [0.9, 0.1, 0.1],
    #       "labels": ["entailment", "contradiction", "neutral"]
    # }
    Tasks.visual_entailment: [OutputKeys.SCORES, OutputKeys.LABELS],

    # {
    #     'labels': ['吸烟', '打电话', '吸烟'],
    #     'scores': [0.7527753114700317, 0.753358006477356, 0.6880350708961487],
    #     'boxes': [[547, 2, 1225, 719], [529, 8, 1255, 719], [584, 0, 1269, 719]],
    #     'timestamps': [1, 3, 5]
    # }
    Tasks.action_detection: [
        OutputKeys.TIMESTAMPS,
        OutputKeys.LABELS,
        OutputKeys.SCORES,
        OutputKeys.BOXES,
    ],

    # {
    #   'output': [
    #     [{'label': '6527856', 'score': 0.9942756295204163}, {'label': '1000012000', 'score': 0.0379515215754509},
    #      {'label': '13421097', 'score': 2.2825044965202324e-08}],
    #     [{'label': '1000012000', 'score': 0.910681426525116}, {'label': '6527856', 'score': 0.0005046309670433402},
    #      {'label': '13421097', 'score': 2.75914817393641e-06}],
    #     [{'label': '1000012000', 'score': 0.910681426525116}, {'label': '6527856', 'score': 0.0005046309670433402},
    #      {'label': '13421097', 'score': 2.75914817393641e-06}]]
    # }
    Tasks.faq_question_answering: [OutputKeys.OUTPUT],

    # image person reid result for single sample
    #   {
    #       "img_embedding": np.array with shape [1, D],
    #   }
    Tasks.image_reid_person: [OutputKeys.IMG_EMBEDDING],
}

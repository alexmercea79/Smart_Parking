import cv2

from FirstDatas import FirstDatas

if dict['save_video']:
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I',
                                    'D')  # optiuni: ('P','I','M','1'), ('D','I','V','X'), ('M','J','P','G'), ('X',
    # 'V','I','D')
    out = cv2.VideoWriter(fn_out, -1, 25.0, (video_info['width'], video_info['height']))
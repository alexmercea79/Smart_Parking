class Options:
    def __init__(self, text_overlay=True,
                 parking_overlay=True,
                 parking_id_overlay=True,
                 parking_detection=True,
                 motion_detection=True,
                 pedestrian_detection=False,  # putere de procesare marita
                 min_area_motion_contour=500,  # detectare miscare
                 park_laplacian_th=2.8,
                 park_sec_to_wait=4,  # 4 schimbare din rosu in verde si invers
                 start_frame=0,  # inceputul videoclipului
                 show_ids=True,  # numarul locului de parcare
                 classifier_used=True,
                 save_video=False):
        self.save_video = save_video
        self.classifier_used = classifier_used
        self.show_ids = show_ids
        self.park_sec_to_wait = park_sec_to_wait
        self.start_frame = start_frame
        self.park_laplacian_th = park_laplacian_th
        self.min_area_motion_contour = min_area_motion_contour
        self.pedestrian_detection = pedestrian_detection
        self.motion_detection = motion_detection
        self.parking_detection = parking_detection
        self.parking_id_overlay = parking_id_overlay
        self.parking_overlay = parking_overlay
        self.text_overlay = text_overlay

    def get_data(self):
        print('options working')

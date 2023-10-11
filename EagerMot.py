import numpy as np
from scipy.optimize import linear_sum_assignment

class EagerMOT:
    def __init__(self, detections, camera_params, lidar_params):
        self.detections = detections
        self.camera_params = camera_params
        self.lidar_params = lidar_params

        # Initialize the trackers
        self.trackers = {}

    def update(self):
        # Fuse 2D and 3D detections
        fused_detections = self.fuse_detections()

        # Update the trackers
        for detection in fused_detections:
            tracker = self.trackers.get(detection.id, None)
            if tracker is None:
                # Create a new tracker
                tracker = Tracker(detection)
                self.trackers[detection.id] = tracker

            # Update the tracker
            tracker.update(detection)

        # Remove inactive trackers
        for tracker_id in list(self.trackers.keys()):
            tracker = self.trackers[tracker_id]
            if not tracker.is_active():
                del self.trackers[tracker_id]

    def get_tracks(self):
        tracks = []
        for tracker_id in self.trackers.keys():
            tracker = self.trackers[tracker_id]
            track = tracker.get_track()
            tracks.append(track)
        return tracks

    def fuse_detections(self):
        # TODO: Implement a more sophisticated fusion algorithm
        fused_detections = []
        for camera_detection in self.detections["camera"]:
            lidar_detection = self.find_corresponding_lidar_detection(camera_detection)
            fused_detection = Detection(camera_detection.id, camera_detection.bbox, lidar_detection.bbox, camera_detection.confidence, lidar_detection.confidence)
            fused_detections.append(fused_detection)

        return fused_detections

    def find_corresponding_lidar_detection(self, camera_detection):
        # TODO: Implement a more sophisticated matching algorithm
        min_distance = np.inf
        min_distance_lidar_detection = None
        for lidar_detection in self.detections["lidar"]:
            distance = np.linalg.norm(camera_detection.bbox - lidar_detection.bbox)
            if distance < min_distance:
                min_distance = distance
                min_distance_lidar_detection = lidar_detection

        return min_distance_lidar_detection

class Tracker:
    def __init__(self, detection):
        self.detection = detection
        self.track = []

    def update(self, detection):
        self.track.append(detection)

    def get_track(self):
        return self.track

    def is_active(self):
        # TODO: Implement a more sophisticated criteria for determining if the tracker is active
        if len(self.track) < 10:
            return False
        else:
            return True

class Detection:
    def __init__(self, id, bbox, bbox_3d, confidence, confidence_3d):
        self.id = id
        self.bbox = bbox
        self.bbox_3d = bbox_3d
        self.confidence = confidence
        self.confidence_3d = confidence_3d


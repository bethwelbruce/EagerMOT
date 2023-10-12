EagerMOT is a simple object tracking algorithm that fuses 2D and 3D detections from a camera and lidar sensor. It is implemented in Python and uses the scipy.optimize.linear_sum_assignment() function to solve the data association problem.

To use EagerMOT, simply initialize it with a list of detections and a dictionary of camera and lidar parameters. Then, call the update() method to update the tracks. Finally, call the get_tracks() method to get a list of Track objects.

Here is an example of how to use EagerMOT:

Python
import eagermot

# Load the detections
detections = {
    "camera": [
        eagermot.Detection(1, [100, 100, 200, 200], None, 0.9, None),
        eagermot.Detection(2, [300, 300, 400, 400], None, 0.8, None),
    ],
    "lidar": [
        eagermot.Detection(1, [101, 101, 201, 201], None, None, 0.9),
        eagermot.Detection(2, [301, 301, 401, 401], None, None, 0.8),
    ],
}

# Load the camera and lidar parameters
camera_params = {
    "width": 640,
    "height": 480,
    "focal_length": 525,
    "principal_point": [320, 240],
}

lidar_params = {
    "fov": np.radians(120),
    "range": 100.0,
}

# Initialize EagerMOT
eagermot = eagermot.EagerMOT(detections, camera_params, lidar_params)

# Update the tracks
eagermot.update()

# Get the tracks
tracks = eagermot.get_tracks()
Use code with caution. Learn more
The tracks variable will now contain a list of Track objects. Each Track object contains a list of Detection objects, which represent the detections that have been assigned to the track.

To visualize the tracks, you can use the following code:

Python
import matplotlib.pyplot as plt

def visualize_tracks(tracks):
    fig, ax = plt.subplots()
    for track in tracks:
        bbox = track.get_track()[-1].bbox
        ax.rectangle(bbox[0], bbox[1], bbox[2] - bbox[0], bbox[3] - bbox[1], color='red')

    ax.set_aspect('equal')
    plt.show()

visualize_tracks(tracks)
Use code with caution. Learn more
This will produce an image showing the tracks of the two objects.

Limitations

The EagerMOT algorithm is a simple algorithm and does not have all of the features of more sophisticated tracking algorithms. For example, it does not handle occlusion or track merging and splitting.

Future work

Some future work for the EagerMOT algorithm includes:

Implementing a more sophisticated fusion algorithm
Implementing a more sophisticated criteria for determining if a tracker is active
Handling occlusion
Handling track merging and splitting

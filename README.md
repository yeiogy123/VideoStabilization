Video Stabilization Application
This application is designed for video stabilization using a graphical user interface built with PyQt5. The application provides functionalities to load a video, mark frames, process stabilization, and playback the stabilized video.

Features
Load a video file.
Display original and stabilized frames.
Progress through frames using a slider.
Mark frames for stabilization processing.
Control parameters for wrapping and smoothing during stabilization.
Play the stabilized video using a built-in media player.
UI Layout
The main window of the application contains the following components:

Function Tab
Load Video: A button to load a video file.
FileName: A label to display the name of the loaded video file.
OriginalFrameProgressBar: A slider to navigate through the frames of the loaded video.
OriginalFrameNumber: A label to display the current frame number and total frames.
Move To Previous Frame: A button to move to the previous frame.
Wrap To Previous Frame: A button to toggle wrapping to the previous frame.
Smooth: A button to toggle smoothing.
Set Red Marker: A button to set a marker on the current frame.
Reset Marker: A button to reset all markers.
Process: A button to start the stabilization process.
StabilizationProgressBar: A progress bar to show the progress of the stabilization process.
CustomGraphicsView: A widget to display the original and stabilized frames.
Video Tab
QVideoWidget: A widget to display the video playback.
Play: A button to play the combined stabilized video.
Slots and Signals
LoadVideo.clicked.connect(self.loadVideo): Connects the "Load Video" button to the loadVideo function.
OriginalFrameProgressBar.valueChanged['int'].connect(self.updateFrame): Updates the displayed frame as the slider value changes.
Process.clicked.connect(self.stabilization): Connects the "Process" button to the stabilization function.
ProcessFrameProgressBar.valueChanged['int'].connect(self.updateStabilizedFrame): Updates the displayed stabilized frame as the slider value changes.
pushButton.clicked.connect(self.startMarking): Connects the "Set Red Marker" button to the startMarking function.
ResetMarkerButton.clicked.connect(self.resetMarker): Connects the "Reset Marker" button to the resetMarker function.
Play.clicked.connect(self.playVideo): Connects the "Play" button to the playVideo function.
SmoothButton.clicked.connect(self.smoothStatus): Connects the "Smooth" button to the smoothStatus function.
WrappingButton.clicked.connect(self.wrappingStatus): Connects the "Wrap To Previous Frame" button to the wrappingStatus function.
SelectPreviousFrame.clicked.connect(self.SelectNumber): Connects the "Move To Previous Frame" button to the SelectNumber function.
FunctionAndVideoTab.currentChanged.connect(self.FunctionAndVideoTabOnTabChanged): Updates the UI when switching between tabs.
Attributes
self.frames: List to store the original frames.
self.stabilizedFrames: List to store the stabilized frames.
self.videoPath: Path to the loaded video file.
self.totalFrames: Total number of frames in the video.
self.wrapping: Flag to indicate if wrapping to the previous frame is enabled.
self.smoothing: Flag to indicate if smoothing is enabled.
Functions
setupUi(self, Stabilization): Sets up the UI components and layout.
retranslateUi(self, Stabilization): Translates the UI text to the appropriate language.
loadVideo(self): Loads the video file and initializes frame processing.
updateFrame(self, value): Updates the displayed original frame based on the slider value.
stabilization(self): Processes the video stabilization.
updateStabilizedFrame(self, value): Updates the displayed stabilized frame based on the slider value.
startMarking(self): Starts marking the current frame.
resetMarker(self): Resets all markers.
playVideo(self): Plays the combined stabilized video.
smoothStatus(self): Toggles smoothing status.
wrappingStatus(self): Toggles wrapping status.
SelectNumber(self): Selects the previous frame based on the input number.
FunctionAndVideoTabOnTabChanged(self, index): Handles tab change events.
Usage
Load Video: Click the "Load Video" button and select a video file.
Navigate Frames: Use the "Move To Previous Frame" button and the slider to navigate through the video frames.
Set Markers: Use the "Set Red Marker" button to mark frames for stabilization.
Process Video: Click the "Process" button to start the stabilization process.
Play Video: Switch to the "Combined Video" tab and click the "Play" button to play the stabilized video.
Dependencies
PyQt5
QtMultimedia
QtMultimediaWidgets

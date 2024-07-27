# -*- coding: utf-8 -*-
import os
import numpy as np
import cv2
# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QMessageBox


class UiStabilization(object):
    def setupUi(self, Stabilization):
        Stabilization.setObjectName("Stabilization")
        Stabilization.resize(1500, 1080)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        Stabilization.setFont(font)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Stabilization)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 1911, 1071))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.TotalVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.TotalVLayout.setContentsMargins(0, 0, 0, 0)
        self.TotalVLayout.setObjectName("TotalVLayout")
        self.TotalHLayout = QtWidgets.QHBoxLayout()
        self.TotalHLayout.setObjectName("TotalHLayout")
        self.FunctionAndVideoTab = QtWidgets.QTabWidget(self.verticalLayoutWidget_2)
        self.FunctionAndVideoTab.setObjectName("FunctionAndVideoTab")
        self.FunctionTab = QtWidgets.QWidget()
        self.FunctionTab.setObjectName("FunctionTab")
        self.FunctionGroupBox = QtWidgets.QGroupBox(self.FunctionTab)
        self.FunctionGroupBox.setGeometry(QtCore.QRect(950, 10, 521, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FunctionGroupBox.sizePolicy().hasHeightForWidth())
        self.FunctionGroupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.FunctionGroupBox.setFont(font)
        self.FunctionGroupBox.setObjectName("FunctionGroupBox")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.FunctionGroupBox)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 30, 501, 441))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.FunctionGroupVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.FunctionGroupVLayout.setContentsMargins(0, 0, 0, 0)
        self.FunctionGroupVLayout.setObjectName("FunctionGroupVLayout")
        self.FunctionGroupH1Layout = QtWidgets.QHBoxLayout()
        self.FunctionGroupH1Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.FunctionGroupH1Layout.setObjectName("FunctionGroupH1Layout")
        self.LoadVideo = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LoadVideo.setFont(font)
        self.LoadVideo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LoadVideo.setAutoRepeat(False)
        self.LoadVideo.setAutoExclusive(False)
        self.LoadVideo.setAutoRepeatInterval(95)
        self.LoadVideo.setDefault(True)
        self.LoadVideo.setObjectName("LoadVideo")
        self.FunctionGroupH1Layout.addWidget(self.LoadVideo)
        self.VideoName = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.VideoName.setFont(font)
        self.VideoName.setAlignment(QtCore.Qt.AlignCenter)
        self.VideoName.setObjectName("VideoName")
        self.FunctionGroupH1Layout.addWidget(self.VideoName)
        self.FunctionGroupVLayout.addLayout(self.FunctionGroupH1Layout)
        self.FunctionGroupH2Layout = QtWidgets.QHBoxLayout()
        self.FunctionGroupH2Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.FunctionGroupH2Layout.setObjectName("FunctionGroupH2Layout")
        self.OriginalFrameProgressBar = QtWidgets.QSlider(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OriginalFrameProgressBar.sizePolicy().hasHeightForWidth())
        self.OriginalFrameProgressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.OriginalFrameProgressBar.setFont(font)
        self.OriginalFrameProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.OriginalFrameProgressBar.setObjectName("OriginalFrameProgressBar")
        self.FunctionGroupH2Layout.addWidget(self.OriginalFrameProgressBar)
        self.OriginalFrameNumber_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.OriginalFrameNumber_3.setFont(font)
        self.OriginalFrameNumber_3.setAlignment(QtCore.Qt.AlignCenter)
        self.OriginalFrameNumber_3.setObjectName("OriginalFrameNumber_3")
        self.FunctionGroupH2Layout.addWidget(self.OriginalFrameNumber_3)
        self.FunctionGroupVLayout.addLayout(self.FunctionGroupH2Layout)
        self.FunctionGroupH3Layout = QtWidgets.QHBoxLayout()
        self.FunctionGroupH3Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.FunctionGroupH3Layout.setObjectName("FunctionGroupH3Layout")
        self.SelectPreviousFrame = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectPreviousFrame.sizePolicy().hasHeightForWidth())
        self.SelectPreviousFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SelectPreviousFrame.setFont(font)
        self.SelectPreviousFrame.setObjectName("SelectPreviousFrame")
        self.FunctionGroupH3Layout.addWidget(self.SelectPreviousFrame)
        self.SelectPreviousFrameNumber = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectPreviousFrameNumber.sizePolicy().hasHeightForWidth())
        self.SelectPreviousFrameNumber.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.SelectPreviousFrameNumber.setFont(font)
        self.SelectPreviousFrameNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.SelectPreviousFrameNumber.setObjectName("SelectPreviousFrameNumber")
        self.FunctionGroupH3Layout.addWidget(self.SelectPreviousFrameNumber)
        self.FunctionGroupVLayout.addLayout(self.FunctionGroupH3Layout)
        self.FunctionGroupH4Layout = QtWidgets.QHBoxLayout()
        self.FunctionGroupH4Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.FunctionGroupH4Layout.setObjectName("FunctionGroupH4Layout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.FunctionGroupH4Layout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.FunctionGroupH4Layout.addWidget(self.pushButton_2)
        self.FunctionGroupVLayout.addLayout(self.FunctionGroupH4Layout)
        self.FunctionGroupH5Layout = QtWidgets.QHBoxLayout()
        self.FunctionGroupH5Layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.FunctionGroupH5Layout.setObjectName("FunctionGroupH5Layout")
        self.Process = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.Process.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Process.sizePolicy().hasHeightForWidth())
        self.Process.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Process.setFont(font)
        self.Process.setObjectName("Process")
        self.FunctionGroupH5Layout.addWidget(self.Process)
        self.StabilizationProgressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StabilizationProgressBar.sizePolicy().hasHeightForWidth())
        self.StabilizationProgressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.StabilizationProgressBar.setFont(font)
        self.StabilizationProgressBar.setProperty("value", 0)
        self.StabilizationProgressBar.setObjectName("StabilizationProgressBar")
        self.FunctionGroupH5Layout.addWidget(self.StabilizationProgressBar)
        self.FunctionGroupVLayout.addLayout(self.FunctionGroupH5Layout)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.FunctionTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 480, 941, 541))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.BeforeStabilizedVLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.BeforeStabilizedVLayout.setContentsMargins(0, 0, 0, 0)
        self.BeforeStabilizedVLayout.setObjectName("BeforeStabilizedVLayout")
        self.BeforeStabilizedTab = QtWidgets.QTabWidget(self.FunctionTab)
        self.BeforeStabilizedTab.setGeometry(QtCore.QRect(0, 490, 940, 540))
        self.BeforeStabilizedTab.setObjectName("BeforeStabilizedTab")
        self.OriginalFrameWidget = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.OriginalFrameWidget.setFont(font)
        self.OriginalFrameWidget.setObjectName("OriginalFrameWidget")
        self.ShowOriginalFrame = QtWidgets.QGraphicsView(self.OriginalFrameWidget)
        self.ShowOriginalFrame.setGeometry(QtCore.QRect(140, 0, 640, 450))
        self.ShowOriginalFrame.setObjectName("ShowOriginalFrame")
        self.layoutWidget = QtWidgets.QWidget(self.OriginalFrameWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 460, 641, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.OriginalFrameHLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.OriginalFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.OriginalFrameHLayout.setObjectName("OriginalFrameHLayout")
        self.ProcessFrameProgressBar = QtWidgets.QSlider(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(36)
        self.ProcessFrameProgressBar.setFont(font)
        self.ProcessFrameProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.ProcessFrameProgressBar.setObjectName("ProcessFrameProgressBar")
        self.OriginalFrameHLayout.addWidget(self.ProcessFrameProgressBar)
        self.OriginalFrameNumber = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.OriginalFrameNumber.setFont(font)
        self.OriginalFrameNumber.setObjectName("OriginalFrameNumber")
        self.OriginalFrameHLayout.addWidget(self.OriginalFrameNumber)
        self.BeforeStabilizedTab.addTab(self.OriginalFrameWidget, "")
        self.tabWidget = QtWidgets.QTabWidget(self.FunctionTab)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 940, 490))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.StabilizedFrame = QtWidgets.QGraphicsView(self.tab_3)
        self.StabilizedFrame.setGeometry(QtCore.QRect(140, 0, 640, 450))
        self.StabilizedFrame.setObjectName("StabilizedFrame")
        self.tabWidget.addTab(self.tab_3, "")
        self.FunctionAndVideoTab.addTab(self.FunctionTab, "")
        self.VideoTab = QtWidgets.QWidget()
        self.VideoTab.setObjectName("VideoTab")
        self.VideoView = QtWidgets.QGraphicsView(self.VideoTab)
        self.VideoView.setGeometry(QtCore.QRect(110, 220, 1280, 480))
        self.VideoView.setObjectName("VideoView")
        self.Play = QtWidgets.QPushButton(self.VideoTab)
        self.Play.setGeometry(QtCore.QRect(750, 700, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Play.setFont(font)
        self.Play.setObjectName("Play")
        self.FunctionAndVideoTab.addTab(self.VideoTab, "")
        self.TotalHLayout.addWidget(self.FunctionAndVideoTab)
        self.TotalVLayout.addLayout(self.TotalHLayout)

        self.retranslateUi(Stabilization)
        self.LoadVideo.clicked.connect(self.loadVideo)
        self.OriginalFrameProgressBar.valueChanged['int'].connect(self.updateFrame)
        self.Process.clicked.connect(self.stabilization)
        self.ProcessFrameProgressBar.valueChanged['int'].connect(self.updateStabilizedFrame)
        self.FunctionAndVideoTab.setCurrentIndex(0)
        self.BeforeStabilizedTab.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Stabilization)

        self.frames = []
        self.stabilizedFrames = []
        self.videoPath = ""
        self.totalFrames = 0
    def retranslateUi(self, Stabilization):
        _translate = QtCore.QCoreApplication.translate
        Stabilization.setWindowTitle(_translate("Stabilization", "Stabilization"))
        self.FunctionGroupBox.setTitle(_translate("Stabilization", "Function"))
        self.LoadVideo.setText(_translate("Stabilization", "Load Video"))
        self.VideoName.setText(_translate("Stabilization", "FileName: "))
        self.OriginalFrameNumber_3.setText(_translate("Stabilization", "0/0"))
        self.SelectPreviousFrame.setText(_translate("Stabilization", "Move To Previous Frame"))
        self.pushButton.setText(_translate("Stabilization", "Red Marker"))
        self.pushButton_2.setText(_translate("Stabilization", "Reset Marker"))
        self.Process.setText(_translate("Stabilization", "Process"))
        self.OriginalFrameNumber.setText(_translate("Stabilization", "0/0"))
        self.BeforeStabilizedTab.setTabText(self.BeforeStabilizedTab.indexOf(self.OriginalFrameWidget), _translate("Stabilization", "Before"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Stabilization", "After"))
        self.FunctionAndVideoTab.setTabText(self.FunctionAndVideoTab.indexOf(self.FunctionTab), _translate("Stabilization", "Stabilization"))
        self.Play.setText(_translate("Stabilization", "Play"))
        self.FunctionAndVideoTab.setTabText(self.FunctionAndVideoTab.indexOf(self.VideoTab), _translate("Stabilization", "Combined Video"))

    def stabilization(self):
        if self.videoPath:
            outputPath = self.videoPath[:-4] + '_stabilized.mp4'
            referenceFrameNo = self.OriginalFrameProgressBar.value()
            self.thread = QtCore.QThread()
            self.worker = StabilizationWorker(self.videoPath, outputPath, referenceFrameNo)
            self.worker.moveToThread(self.thread)
            self.worker.progress.connect(self.StabilizationProgressBar.setValue)
            #self.worker.progress.connect(self.updateProgressAndFrames)  # Connect to the new slot
            self.worker.finished.connect(self.handleStabilizedFrames)  # Connect to the new slot
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        else:
            QMessageBox.warning(None, "Warning", "Please choose a video first.")

    def updateProgressAndFrames(self, progress):
        self.StabilizationProgressBar.setValue(progress)
        self.updateStabilizedFrame(progress)
    def handleStabilizedFrames(self, frameStabilized):
        # Handle the stabilized frames
        self.stabilizedFrames = frameStabilized
        # Update the GUI accordingly, for example, show the first stabilized frame
        self.updateStabilizedFrame(0)
    def loadVideo(self):
        options = QFileDialog.Options()
        fileName = ""
        try:
            fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;MP4 Files (*.mp4)", options=options)
        except Exception as e:
            print(e)

        if fileName is not None:
            print("fileName= ", fileName)
            self.videoPath = fileName
            self.frames = self.extractFrames(fileName)
            self.VideoName.setText("FileName: "+ os.path.basename(fileName))
            self.totalFrames = len(self.frames)
            self.OriginalFrameProgressBar.setMaximum(self.totalFrames - 1)
            self.OriginalFrameNumber_3.setText(f"0/{self.totalFrames}")
            self.updateFrame(0)
        else:
            print("No File Selected")
    def extractFrames(self, videoPath):
        cap = cv2.VideoCapture(videoPath)
        frames = []
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        cap.release()
        return frames

    def updateStabilizedFrame(self, frame_idx):
        self.ShowOriginalFrame.scene().clear()
        frame = self.stabilizedFrames[frame_idx]
        frame = cv2.resize(frame, (640, 480))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_img = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_img)
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.StabilizedFrame.setScene(scene)
        self.OriginalFrameNumber.setText(f"{frame_idx + 1}/{self.totalFrames - self.OriginalFrameProgressBar.value()}")

        frame = self.frames[frame_idx + self.OriginalFrameProgressBar.value()]
        frame = cv2.resize(frame, (640, 480))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_img = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_img)
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.ShowOriginalFrame.setScene(scene)

    def updateFrame(self, frame_idx):
        frame = self.frames[frame_idx]
        frame = cv2.resize(frame, (640, 480))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_img = QtGui.QImage(frame.data, width, height, bytes_per_line, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(q_img)
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.ShowOriginalFrame.setScene(scene)
        self.OriginalFrameNumber_3.setText(f"{frame_idx + 1}/{self.totalFrames}")

class StabilizationWorker(QtCore.QObject):
    progress = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal(list)

    def __init__(self, inputPath, outputPath, referenceFrameNo):
        super().__init__()
        self.inputPath = inputPath
        self.outputPath = outputPath
        self.referenceFrameNo = referenceFrameNo

    def run(self):
        frameStabilized = self.usingSIFTWithRansac(self.progress)
        self.finished.emit(frameStabilized)

    def movingAverage(self, curve, radius):
        window_size = 2 * radius + 1
        # Define the filter
        f = np.ones(window_size) / window_size
        # Add padding to the boundaries
        curve_pad = np.lib.pad(curve, (radius, radius), 'edge')
        # Apply convolution
        curve_smoothed = np.convolve(curve_pad, f, mode='same')
        # Remove padding
        curve_smoothed = curve_smoothed[radius:-radius]
        # return smoothed curve
        return curve_smoothed

    def smooth(self, trajectoryy):
        smoothed_trajectory = np.copy(trajectoryy)
        # Filter the x, y and angle curves
        for ii in range(3):
            smoothed_trajectory[:, ii] = self.movingAverage(trajectoryy[:, ii], radius=100)  # 100CAN CHANGE
        return smoothed_trajectory

    def fixBorder(self, frame):
        s = frame.shape
        # Scale the image 4% without moving the center
        T = cv2.getRotationMatrix2D((s[1] / 2, s[0] / 2), 0, 1.04)
        frame = cv2.warpAffine(frame, T, (s[1], s[0]))
        return frame

    def usingSIFTWithRansac(self, progress):
        cap = cv2.VideoCapture(self.inputPath)
        sift = cv2.SIFT_create()
        flann_params = dict(algorithm=1, trees=5)
        flann = cv2.FlannBasedMatcher(flann_params, {})
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.set(cv2.CAP_PROP_POS_FRAMES, self.referenceFrameNo)
        ret, prev_frame = cap.read()
        prev_frame_resized = cv2.resize(prev_frame, (640, 480))
        prev_gray = cv2.cvtColor(prev_frame_resized, cv2.COLOR_BGR2GRAY)
        prev_kp, prev_des = sift.detectAndCompute(prev_gray, None)
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        out = cv2.VideoWriter(self.outputPath, fourcc, cap.get(cv2.CAP_PROP_FPS), (1280, 480))
        frame_count = 0
        n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        transforms = np.zeros((n_frames - 1, 3), np.float32)
        for i in range(n_frames - self.referenceFrameNo - 2):
            ret, frame = cap.read()
            frame_resized = cv2.resize(frame, (640, 480))
            gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)
            kp, des = sift.detectAndCompute(gray, None)
            matches = flann.knnMatch(prev_des, des, k=2)
            good_matches = [m for m, n in matches if m.distance < 0.3 * n.distance]
            src_pts = np.float32([prev_kp[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            M, mask = cv2.estimateAffinePartial2D(src_pts, dst_pts, method=cv2.RANSAC)
            dx = M[0, 2]
            dy = M[1, 2]
            # Extract rotation angle
            da = np.arctan2(M[1, 0], M[0, 0])
            transforms[i] = [dx, dy, da]
            prev_kp, prev_des = kp, des
            frame_count += 1
            progress.emit(frame_count * 100 // total_frames // 2)

        # Compute trajectory using cumulative sum of transformations
        trajectory = np.cumsum(transforms, axis=0)
        # Calculate difference in smoothed_trajectory and trajectory
        smoothed_trajectory = self.smooth(trajectory)
        difference = smoothed_trajectory - trajectory
        # Calculate newer transformation array
        transforms_smooth = transforms + difference
        # Reset stream to first frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, self.referenceFrameNo)
        frameStabilized = []
        # Write n_frames-1 transformed frames
        for i in range(n_frames - self.referenceFrameNo - 2):
            success, frame = cap.read()
            if i == 0:
                frame = cv2.resize(frame, (640, 480))
                frameStabilized.append(frame)
                out.write(frame)
            else:
                # Extract transformations from the new transformation array
                dx = transforms_smooth[i, 0]
                dy = transforms_smooth[i, 1]
                da = transforms_smooth[i, 2]
                # Reconstruct transformation matrix accordingly to new values
                m = np.zeros((2, 3), np.float32)
                m[0, 0] = np.cos(da)
                m[0, 1] = -np.sin(da)
                m[1, 0] = np.sin(da)
                m[1, 1] = np.cos(da)
                m[0, 2] = dx
                m[1, 2] = dy
                # Apply affine wrapping to the given frame
                frame = cv2.resize(frame, (640, 480))
                frame_stabilized = cv2.warpAffine(frame, m, (640, 480))
                frame_stabilized = self.fixBorder(frame_stabilized)
                frameStabilized.append(frame_stabilized)
                frame_out = cv2.hconcat([frame, frame_stabilized])
                out.write(frame_out)
            frame_count += 1
            progress.emit(frame_count * 100 // total_frames // 2)
        out.release()
        cap.release()
        progress.emit(100)
        return frameStabilized


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stabilization = QtWidgets.QWidget()
    ui = UiStabilization()
    ui.setupUi(Stabilization)
    Stabilization.show()
    sys.exit(app.exec_())

import subprocess as sp
import cv2

adbCmd = ['adb', 'exec-out', 'screenrecord', '--output-format=h264', '-']
stream = sp.Popen(adbCmd, stdout = sp.PIPE)

#ffmpegCmd =['ffmpeg', '-i', '-', '-f', 'rawvideo', '-vf', 'scale=324:576', '-vcodec', 'bmp',  '-']
#ffmpeg = sp.Popen(ffmpegCmd, stdin = stream.stdout, stdout = sp.PIPE)

ffmpegCmd = ['ffmpeg', '-i', '-', '-f', 'rawvideo', '-vcodec', 'bmp', '-vf', 'fps=5', '-']
ffmpeg = sp.Popen(ffmpegCmd, stdin = stream.stdout, stdout = sp.PIPE)

while True:
    '''
    fileSizeBytes = ffmpeg.stdout.read(6)
    fileSize = 0
    for i in xrange(4):
        fileSize += array.array('B',fileSizeBytes[i + 2])[0] * 256 ** i
    bmpData = fileSizeBytes + ffmpeg.stdout.read(fileSize - 6)
    image = cv2.imdecode(np.fromstring(bmpData, dtype = np.uint8), 1)
    '''
    fileSizeBytes = ffmpeg.stdout.read(6)
    fileSize = 0
    for i in xrange(4):
        fileSize += fileSizeBytes[i + 2] * 256 ** i
    bmpData = fileSizeBytes + ffmpeg.stdout.read(fileSize - 6)
    image = cv2.imdecode(np.fromstring(bmpData, dtype = np.uint8), 1)
    cv2.imshow("im",image) 
    cv2.waitKey(25)

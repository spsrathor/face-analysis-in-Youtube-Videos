from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=V-H2RNPFBME')
print(yt)
print('*************************************')
print(yt.title)
print('**************Filtering**************')
yt.streams.filter(file_extension='mp4')
print('**************FilterED**************')
print(type(yt.streams))
print('*************************************')
stream = yt.streams.get_by_itag(22)
stream.download(filename='file.mp4')
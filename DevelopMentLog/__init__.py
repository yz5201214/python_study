import json,re,operator

if __name__ == '__main__':
    abc = '[{"file_name": "The Untamed.2019.EP01-08.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_0.torrent", "file_size": "148.50K"}, {"file_name": "The Untamed.2019.EP09-10.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_1.torrent", "file_size": "82.55K"}, {"file_name": "The Untamed.2019.EP11-14.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_2.torrent", "file_size": "83.04K"}, {"file_name": "The Untamed.2019.EP15-20.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_3.torrent", "file_size": "121.67K"}, {"file_name": "The Untamed.2019.EP21-22.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_4.torrent", "file_size": "83.16K"}, {"file_name": "The Untamed.2019.EP23-24.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_5.torrent", "file_size": "82.90K"}, {"file_name": "The Untamed.2019.EP25-26.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_6.torrent", "file_size": "83.47K"}, {"file_name": "The Untamed.2019.EP27-28.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_7.torrent", "file_size": "83.23K"}, {"file_name": "The Untamed.2019.EP29-30.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_8.torrent", "file_size": "83.31K"}, {"file_name": "The Untamed.2019.EP31-32.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_9.torrent", "file_size": "83.64K"}, {"file_name": "The Untamed.2019.EP33-38.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_10.torrent", "file_size": "124.56K"}, {"file_name": "The Untamed.2019.EP39-42.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_11.torrent", "file_size": "85.38K"}, {"file_name": "The Untamed.2019.EP43-44.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_12.torrent", "file_size": "84.93K"}, {"file_name": "The Untamed.2019.EP45-46.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_13.torrent", "file_size": "86.42K"}, {"file_name": "The Untamed.2019.EP47-48.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_14.torrent", "file_size": "81.65K"}, {"file_name": "The Untamed.2019.EP49-50.WEB-DL.1080p.HEVC.AAC-HQC.torrent", "file_url": "drama/2019/thread-index-fid-950-tid-4495641.htm/thread-index-fid-950-tid-4495641.htm_15.torrent", "file_size": "83.47K"}]'
    testa = json.loads(abc)
    print(testa)

    testa = ['2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2'
 '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '2' '1' '1' '1' '1' '1' '1'
 '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1'
 '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1'
 '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1' '1']
    print(testa.index('2'))





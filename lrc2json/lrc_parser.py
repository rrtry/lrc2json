import re
from typing import TextIO

class LRC:

    def __init__(self, file: TextIO):
        self.file = file
    
    def write_synced_lyrics(self, lyrics: dict, f: TextIO) -> None:
        
        for millis in sorted(lyrics.keys()):

            minutes   = millis // 1000 // 60 
            seconds   = (millis // 1000) % 60
            remainder = millis % 1000

            line = '[{:02d}:{:02d}.{:02d}]{}'.format(minutes, seconds, remainder, lyrics[millis])
            if line[-1] != '\n': line += '\n'
            f.write(line)
    
    def get_synced_lyrics(self) -> dict:

        lines = self.file.readlines()
        synced_lyrics_dict = {}

        for lrc_line in lines:
            
            if len(lrc_line) == 0:
                continue
            
            results = re.finditer('(\[\d\d\:\d\d\.\d+?(?=\])\]+)|(\[\d\d\:\d+?(?=\])\]+)', lrc_line)
            matches = [t for t in results]

            if len(matches) == 0:
                continue

            end_index    = max([t.end(0) for t in matches])
            lyrics       = lrc_line[end_index:]
            s_timestamps = [t.group(0) for t in matches]
            
            for s_timestamp in s_timestamps:

                s_timestamp = s_timestamp[1:-1]
                
                minutes = 0
                seconds = 0
                millis  = 0

                has_millis = '.' in s_timestamp
                pattern    = '[\.:]' if has_millis else ':'
                parts      = re.split(pattern, s_timestamp)

                minutes = int(parts[0])
                seconds = int(parts[1])

                if has_millis:
                    millis = int(parts[2])

                timestamp = minutes * 60 * 1000 + seconds * 1000 + millis
                synced_lyrics_dict[timestamp] = lyrics

        return synced_lyrics_dict     
    
    
                

        
        
        
    

    
        
    

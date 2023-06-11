import argparse
import json
from lrc_parser import *

def main():

    parser = argparse.ArgumentParser(
                    prog='lrc2json',
                    description='Convert LRC format into json with timestamps',
                    usage="lrc2json: <lrc_file> <json_file>")
    
    parser.add_argument("lrc_file")
    parser.add_argument("json_file")
    args = parser.parse_args()

    in_f   = open(args.lrc_file, "r", encoding="UTF-8")
    lrc    = LRC(in_f)
    lyrics = lrc.get_synced_lyrics()

    out_f = open(args.json_file, "w", encoding="UTF-8")
    out_f.write(json.dumps(lyrics))

    in_f.close()
    out_f.close()

if __name__ == "__main__":
    main()



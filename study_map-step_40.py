# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: StudyMap
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="StudyMap CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)
    
    p_show = sub.add_parser("show", help="show progress")
    p_show.add_argument("--topic", help="filter by topic")
    
    p_learn = sub.add_parser("learn", help="start a topic")
    p_learn.add_argument("topic", help="topic name")
    
    p_test = sub.add_parser("test", help="take a quiz")
    p_test.add_argument("topic", help="topic name")
    
    p_reset = sub.add_parser("reset", help="reset progress")
    p_reset.add_argument("--topic", help="reset specific topic")
    
    return parser.parse_args()

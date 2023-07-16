#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', help='Path to first file')
    parser.add_argument('second_file', help='Path to first file')

    parser.parse_args()
    # args = parser.parse_args()


if __name__ == '__main__':
    main()

from multiprocessing import Pool
import glob
import os

NUM_PARARREL = 2
INPUT_FILES_DIR = "data_in"
OUTPUT_FILES_DIR = "data_out"


def f(input_file):
    filename = input_file.split("/")[-1]
    print(filename)

    print(f"Scraping {filename}...")
    os.system(f"./scrape.sh --input_file {input_file} --output_file {OUTPUT_FILES_DIR}/{filename}")
    print(f"Scraping {filename} complete!")

if __name__ == '__main__':
    os.makedirs(OUTPUT_FILES_DIR, exist_ok=True)

    files_to_scrape = glob.glob(f"{INPUT_FILES_DIR}/*")
    with Pool(NUM_PARARREL) as p:
        p.map(f, files_to_scrape)
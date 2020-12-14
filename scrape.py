from multiprocessing import Pool
import glob
import os

NUM_PARARREL = 2

def f(input_file):
    filename = input_file.split("/")[-1]
    print(filename)

    print(f"Scraping {filename}...")
    os.system(f"./scrape.sh --input_file {input_file} --output_file data_out/{filename}")
    print(f"Scraping {filename} complete!")

if __name__ == '__main__':
    os.makedirs("data_out", exist_ok=True)

    files_to_scrape = glob.glob("data_in/*")
    with Pool(NUM_PARARREL) as p:
        p.map(f, files_to_scrape)
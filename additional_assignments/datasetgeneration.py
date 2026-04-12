import os
from icrawler.builtin import BingImageCrawler

# Define your classes and their corresponding search queries
categories = {
    "wet_waste": ["organic waste food", "rotting vegetables garbage", "wet garbage bag"],
    "dry_waste": ["recyclable plastic bottles", "cardboard paper waste", "dry trash metal cans"],
    "electronic_waste": ["discarded electronics", "broken mobile phones e-waste", "e-waste computer parts"]
}

dataset_dir = "garbage_dataset"
images_per_query = 100  # Adjust this based on how large you want your dataset

def build_dataset(base_dir, categories_dict):
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    for category, queries in categories_dict.items():
        # Create a directory for each class
        class_dir = os.path.join(base_dir, category)
        if not os.path.exists(class_dir):
            os.makedirs(class_dir)
            
        print(f"--- Fetching images for: {category} ---")
        
        for query in queries:
            # Initialize the crawler
            crawler = BingImageCrawler(storage={'root_dir': class_dir})
            # Scrape images based on the specific query
            crawler.crawl(keyword=query, max_num=images_per_query)

if __name__ == "__main__":
    build_dataset(dataset_dir, categories)
    print("Dataset generation complete!")
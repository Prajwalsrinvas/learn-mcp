import json, os
from datetime import datetime
import pandas as pd

class dataProcessor:
    def __init__(self, file_path):
        self.filePath = file_path
        self.data = None
        self.processed_data = None
    
    def load_data(self):
        if os.path.exists(self.filePath):
            with open(self.filePath, 'r') as f:
                self.data = json.load(f)
                return True
        else:
            print("File not found!")
            return False
    
    def processData(self):
        if self.data is None:
            return None
        
        processed = []
        for item in self.data:
            if 'timestamp' in item and 'value' in item:
                # Convert timestamp to datetime
                dt = datetime.fromisoformat(item['timestamp'])
                
                # Calculate some metrics
                processed_item = {
                    'original_value': item['value'],
                    'processed_value': item['value'] * 1.1 if item['value'] > 0 else 0,
                    'date': dt.strftime('%Y-%m-%d'),
                    'hour': dt.hour,
                    'is_weekend': dt.weekday() >= 5
                }
                processed.append(processed_item)
        
        self.processed_data = processed
        return processed
    
    def save_to_csv(self, output_path):
        if self.processed_data:
            df = pd.DataFrame(self.processed_data)
            df.to_csv(output_path, index=False)
            print(f"Data saved to {output_path}")
        else:
            print("No processed data available")
    
    def get_summary_stats(self):
        if not self.processed_data: return None
        
        values = [item['processed_value'] for item in self.processed_data]
        return {
            'count': len(values),
            'mean': sum(values) / len(values) if values else 0,
            'max': max(values) if values else 0,
            'min': min(values) if values else 0
        }

def main():
    processor = dataProcessor('data.json')
    
    if processor.load_data():
        results = processor.processData()
        if results:
            print(f"Processed {len(results)} items")
            stats = processor.get_summary_stats()
            print("Summary statistics:", stats)
            processor.save_to_csv('output.csv')
    else:
        print("Failed to process data")

if __name__ == '__main__':
    main()
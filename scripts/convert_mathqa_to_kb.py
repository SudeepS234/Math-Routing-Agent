from datasets import load_dataset
import re

def clean_text(text):
    """Clean and format text by removing extra spaces and formatting"""
    # Remove multiple spaces and clean up
    text = re.sub(r'\s+', ' ', text.strip())
    return text

def extract_answer_letter(correct_answer, options):
    """Extract the actual answer content from the options based on the correct letter"""
    # The correct answer is usually just a letter like 'a', 'b', etc.
    correct_letter = correct_answer.lower().strip()
    
    # Parse options to find the corresponding answer
    # Options format is usually "a ) answer1 , b ) answer2 , ..."
    options_clean = clean_text(options)
    
    # Try to extract the answer corresponding to the correct letter
    pattern = rf'{correct_letter}\s*\)\s*([^,]+?)(?:\s*,\s*[a-e]\s*\)|$)'
    match = re.search(pattern, options_clean, re.IGNORECASE)
    
    if match:
        return match.group(1).strip()
    else:
        # Fallback: just return the letter if we can't parse the options
        return correct_letter.upper()

def clean_explanation(rationale):
    """Clean up the explanation text"""
    # Remove quotes at the beginning and end
    rationale = rationale.strip('"')
    
    # Remove "explanation :" if it exists at the beginning
    rationale = re.sub(r'^explanation\s*:\s*', '', rationale, flags=re.IGNORECASE)
    
    # Remove "answer : [letter]" at the end
    rationale = re.sub(r'answer\s*:\s*[a-e]\s*$', '', rationale, flags=re.IGNORECASE)
    rationale = re.sub(r'answer\s*:\s*option\s*[a-e]\s*$', '', rationale, flags=re.IGNORECASE)
    
    # Clean up spacing
    rationale = clean_text(rationale)
    
    return rationale

def extract_dataset_to_file(output_filename="math_qa_extracted.txt", num_samples=None):
    """
    Extract math QA dataset and save to text file
    
    Args:
        output_filename: Name of the output file
        num_samples: Number of samples to extract (None for all)
    """
    print("Loading dataset...")
    dataset = load_dataset("allenai/math_qa", trust_remote_code=True)
    
    train_data = dataset["train"]
    total_samples = len(train_data) if num_samples is None else min(num_samples, len(train_data))
    
    print(f"Extracting {total_samples} samples...")
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        for i in range(total_samples):
            try:
                ex = train_data[i]
                
                # Extract and clean question
                question = clean_text(ex['Problem'])
                
                # Extract answer
                answer = extract_answer_letter(ex['correct'], ex['options'])
                
                # Extract and clean explanation
                explanation = clean_explanation(ex['Rationale'])
                
                # Write in the specified format
                f.write(f"{question}\n")
                f.write(f"Answer: {answer}\n")
                f.write(f"Explanation: {explanation}\n")
                f.write(f"\n")  # Empty line between questions
                
                # Progress indicator
                if (i + 1) % 1000 == 0:
                    print(f"Processed {i + 1}/{total_samples} samples...")
                    
            except Exception as e:
                print(f"Error processing sample {i}: {e}")
                continue
    
    print(f"Successfully extracted {total_samples} samples to '{output_filename}'")

# Example usage
if __name__ == "__main__":
    # Extract first 100 samples for testing
    extract_dataset_to_file("math_qa_sample.txt", num_samples=5000)
    
    # Uncomment below to extract the entire dataset
    # extract_dataset_to_file("math_qa_full.txt")
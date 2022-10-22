from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from time import time
import torch


class RelationShipExtractor:

    def __init__(self):
        self.gen_kwargs = {
            "max_length": 256,
            "length_penalty": 0,
            "num_beams": 1,
            "num_return_sequences": 1,
        }

        self.tokenizer, self.model, self.dataset = self.load_models()

    def load_models(self):
        st_time = time()
        tokenizer = AutoTokenizer.from_pretrained("Babelscape/rebel-large")
        print("+++++ loading Model", time() - st_time)
        model = AutoModelForSeq2SeqLM.from_pretrained("Babelscape/rebel-large")
        if torch.cuda.is_available():
            _ = model.to("cuda:0") # comment if no GPU available
        _ = model.eval()
        print("+++++ loaded model", time() - st_time)
        dataset = load_dataset('rebel/datasets/rebel-short.py', data_files={'train': 'rebel/data/rebel/sample.jsonl', 'dev': 'rebel/data/rebel/sample.jsonl', 'test': 'rebel/data/rebel/sample.jsonl', 'relations': "rebel/data/relations_count.tsv"}, split="validation")
        return (tokenizer, model, dataset)


    def extract_triplets(self, text):
        triplets = []
        relation = ''
        subject = None
        relation = None
        object_ = None
        current = ''
        for token in text.split():
            if token == "<triplet>":
                current = 't'
                if relation != '':
                    triplets.append((subject, relation, object_))
                    relation = ''
                subject = ''
            elif token == "<subj>":
                current = 's'
                if relation != '':
                    triplets.append((subject, relation, object_))
                object_ = ''
            elif token == "<obj>":
                current = 'o'
                relation = ''
            else:
                if current == 't':
                    subject += ' ' + token
                elif current == 's':
                    object_ += ' ' + token
                elif current == 'o':
                    relation += ' ' + token

        if subject and relation and object_:
            triplets.append((subject, relation, object_))

        return triplets

    def run(self, text):
        triples = []
        model_inputs = self.tokenizer(text, max_length=256, padding=True, truncation=True, return_tensors = 'pt')
        generated_tokens = self.model.generate(
            model_inputs["input_ids"].to(self.model.device),
            attention_mask=model_inputs["attention_mask"].to(self.model.device),
            **self.gen_kwargs,
        )

        decoded_preds = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=False)
        decoded_preds = [text.replace('<s>', '').replace('</s>', '').replace('<pad>', '') for text in decoded_preds]

        for triple in self.extract_triplets(decoded_preds[0]):
            if triple[0] and triple[1] and triple[2]:
                print(triple)
                triples.append(triple)

        return triples

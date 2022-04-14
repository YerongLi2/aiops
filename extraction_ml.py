from monkeylearn import MonkeyLearn

ml = MonkeyLearn('7cfbdb347b316cb465185868e4ec75e145ddb7b4')
data = ["I have to say that this hotel has the worst customer support ever. It is a shame that people in management positions (who should be more respectful of their customers) are rude and have bad attitudes. They completely ruined my vacations."]
model_id = 'ex_YCya9nrn'
result = ml.extractors.extract(model_id, data)
print(result.body)
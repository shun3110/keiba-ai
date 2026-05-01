
import pandas as pd
import lightgbm as lgb
import joblib
from pathlib import Path

data = {
    "popularity":[1,2,3,4,5,6,7,8],
    "odds":[2.1,3.5,4.2,8.8,10.2,15.5,30.1,50.0],
    "weight":[55,56,57,54,55,56,57,58],
    "frame":[1,2,3,4,5,6,7,8],
    "target":[1,1,1,0,0,0,0,0]
}

df = pd.DataFrame(data)

X = df.drop("target", axis=1)
y = df["target"]

model = lgb.LGBMClassifier(
    n_estimators=300,
    learning_rate=0.03
)

model.fit(X, y)

Path("model").mkdir(exist_ok=True)

joblib.dump(model, "model/model.pkl")

print("学習完了")

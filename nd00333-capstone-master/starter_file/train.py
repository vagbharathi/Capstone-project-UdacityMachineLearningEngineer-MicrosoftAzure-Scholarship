{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "import argparse\n",
    "import os\n",
    "import numpy as np\n",
    "from sklearn.metrics import mean_squared_error\n",
    "import joblib\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import OneHotEncoder\n",
    "import pandas as pd\n",
    "from azureml.core.run import Run\n",
    "from azureml.data.dataset_factory import TabularDatasetFactory\n",
    "\n",
    "def clean_data(data):\n",
    "    data = data.to_pandas_dataframe()\n",
    "    y = data['DEATH_EVENT']\n",
    "    x = data.drop('DEATH_EVENT', 1) \n",
    "    return x, y\n",
    "\n",
    "\n",
    "def main():\n",
    "    url_path = \"https://raw.githubusercontent.com/maulingogri/Azure-Udacity-MLE-ND-Capstone/master/data/heart_failure_clinical_records_dataset.csv\"\n",
    "    ds = TabularDatasetFactory.from_delimited_files(path=url_path)\n",
    "\n",
    "    # Split data into train and score sets\n",
    "    # train, score = ds.random_split(percentage=0.75, seed=121)\n",
    "\n",
    "    x, y = clean_data(ds)\n",
    "\n",
    "    # TODO: Split data into train and test sets.\n",
    "    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=121)\n",
    "\n",
    "    run = Run.get_context()\n",
    "\n",
    "    # Add arguments to script\n",
    "    parser = argparse.ArgumentParser()\n",
    "\n",
    "    parser.add_argument('--C', type=float, default=1.0, help=\"Inverse of regularization strength. Smaller values cause stronger regularization\")\n",
    "    parser.add_argument('--max_iter', type=int, default=100, help=\"Maximum number of iterations to converge\")\n",
    "\n",
    "    args = parser.parse_args()\n",
    "\n",
    "    run.log(\"Regularization Strength:\", np.float(args.C))\n",
    "    run.log(\"Max iterations:\", np.int(args.max_iter))\n",
    "\n",
    "    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)\n",
    "    joblib.dump(model, os.path.join('outputs', 'hd_model.joblib'))\n",
    "\n",
    "    accuracy = model.score(x_test, y_test)\n",
    "    run.log(\"Accuracy\", np.float(accuracy))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

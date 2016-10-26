Using these, You can create your own image data set for TensorFlow.

■data_set
  −train.txt
    ・you have to write the location path of train data_set in this
    ・and write Classification Number after " "
    ・and write "\n"
    ・for example
-------train.txt-----------
data_set/test001.jpeg 0
data_set/test002.jpeg 1
data_set/test003.jpeg 2
data_set/test004.jpeg 3
---------------------------
  −test.txt
    ・you have to write the location path of train data_set in this in the same way as "train.txt"

■read_data.py
  To run this, you can get "models/model.ckpt". That ckpt file could be used to "use_model.py"

■use_model.py
  To run this, you can test "models/model.ckpt"(Using test data_set).

■create_data_set.py
cat class0.txt class1.txt class2.txt class3.txt class4.txt > train.txt
cat class0.txt class1.txt class2.txt class3.txt class4.txt > test.txt

you can't use " " in jpg filename
sudo rename "s/ /_/g" *.jpg

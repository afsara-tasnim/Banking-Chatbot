from model import model
from nltk_utilize import training, output

#Loading model/training model
# try:
#   model.load("JanataChat.tflearn")
#
# except:
#    model.fit(
#        training,
#        output,
#        n_epoch=800,
#        batch_size=128,
#        validation_set=(training, output),
#        show_metric=True
#        )
#
#    model.save("JanataChat.tflearn")

#Mute after one run
model.fit(
       training,
       output,
       n_epoch=800,
       batch_size=128,
       validation_set=(training, output),
       show_metric=True
       )

model.save("JanataChat.tflearn")


# Evaluate model
score = model.evaluate(training, output)
print('Test accuracy: %0.4f%%' % (score[0] * 100))
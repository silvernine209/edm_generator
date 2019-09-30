import matplotlib.pyplot as plt

# Don't always choose the most likely prediction
def sample(preds, temperature):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    #classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    #print(cm)

    SMALL_SIZE = 8
    MEDIUM_SIZE = 15
    BIGGER_SIZE = 20

    plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    
 
    fig, ax = plt.subplots(figsize=(30, 30))
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...

    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

def various_scores(model,X,y,data_type):
    pred = model.predict(X)
    print(data_type," Data")
    print('######################################################')
    print("Accuracy : {:.2f} %".format(metrics.accuracy_score(y, pred)*100))
    print('______________________________________________________')
    print(metrics.classification_report(y,pred,digits=2))
    print('______________________________________________________')
    
def plot_song_composition(prediction):
    plt.figure(figsize=(20,20))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False) 
    plt.ylabel('Songs',fontsize=20)
    plt.xlabel('Percentage (%)',fontsize=20)
    plt.title('Song Classification',fontsize=30)
    sns.barplot(y=pd.Series(prediction).value_counts().keys(),
                x=np.round(pd.Series(prediction).value_counts().values/sum(pd.Series(prediction).value_counts().values)*100,2),
                palette="hot")

def plot_genre_composition(prediction):
#     # Load edm file names
#     edm_filenames = os.listdir('data/midi')
#     if '.DS_Store' in edm_filenames:
#         edm_filenames.remove('.DS_Store')
#     # Remove Unnecessary Strings
#     for ix,file in enumerate(edm_filenames):
#         edm_filenames[ix] = edm_filenames[ix].replace('  (midi by Carlo Prato) (www.cprato.com)','')
#         edm_filenames[ix] = edm_filenames[ix].replace(' (midi by Carlo Prato) (www.cprato.com)','')
#         edm_filenames[ix] = edm_filenames[ix].replace('.mid','')   
#     # Load classic file names
#     classic_filenames = os.listdir('data/midi_classic')
#     if '.DS_Store' in classic_filenames:
#         classic_filenames.remove('.DS_Store')
#     for ix,file in enumerate(classic_filenames):
#         classic_filenames[ix] = classic_filenames[ix].replace('.mid','')        
        
#     genre_list = []
#     for i in range(len(prediction)):        
#         if prediction[i] in edm_filenames:
#             genre_list.append('EDM')
#         elif prediction[i] in classic_filenames:
#             genre_list.append('Classic')
    # For NN classifier only
    genre_list = prediction
    
    plt.figure(figsize=(5,5))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False) 
    plt.ylabel('Genre',fontsize=15)
    plt.xlabel('Percentage (%)',fontsize=15)
    plt.title('Genre Classification',fontsize=20)
    sns.barplot(x=pd.Series(genre_list).value_counts().keys(),
                y=np.round(pd.Series(genre_list).value_counts().values/sum(pd.Series(genre_list).value_counts().values)*100,2))   

def plot_song_progression(prediction):
    plt.figure(figsize=(20,20))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False) 
    plt.ylabel('Songs',fontsize=20)
    plt.xlabel('Steps',fontsize=20)
    plt.title('Song Progression',fontsize=30)
    plt.scatter(np.arange(len(prediction)),prediction)
    
def plot_genre_progression(prediction):
#         # Load edm file names
#     edm_filenames = os.listdir('data/midi')
#     if '.DS_Store' in edm_filenames:
#         edm_filenames.remove('.DS_Store')
#     # Remove Unnecessary Strings
#     for ix,file in enumerate(edm_filenames):
#         edm_filenames[ix] = edm_filenames[ix].replace('  (midi by Carlo Prato) (www.cprato.com)','')
#         edm_filenames[ix] = edm_filenames[ix].replace(' (midi by Carlo Prato) (www.cprato.com)','')
#         edm_filenames[ix] = edm_filenames[ix].replace('.mid','')   
#     # Load classic file names
#     classic_filenames = os.listdir('data/midi_classic')
#     if '.DS_Store' in classic_filenames:
#         classic_filenames.remove('.DS_Store')
#     for ix,file in enumerate(classic_filenames):
#         classic_filenames[ix] = classic_filenames[ix].replace('.mid','')        
        
#     genre_list = []
#     for i in range(len(prediction)):        
#         if prediction[i] in edm_filenames:
#             genre_list.append('EDM')
#         elif prediction[i] in classic_filenames:
#             genre_list.append('Classic')
    # For NN classifier
    genre_list = prediction  
    
    plt.figure(figsize=(20,1))
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False) 
    plt.ylabel('Songs',fontsize=15)
    plt.xlabel('Steps',fontsize=15)
    plt.title('Song Progression',fontsize=20)
    plt.scatter(np.arange(len(genre_list)),genre_list)
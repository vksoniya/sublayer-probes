from sklearn.manifold import TSNE

def reduce_dim__per_token(input_vector):
tsne_dim_reducer = TSNE(n_components=2, perplexity=5)
    
	#tsne
	tsne_dim_reduced_vector = tsne_dim_reducer.fit_transform(np.array(input_vector))
	tsne_df_dim_reduced = pd.DataFrame.from_dict({'x':tsne_dim_reduced_vector[:,0],'y':tsne_dim_reduced_vector[:,1]})
    
return tsne_df_dim_reduced

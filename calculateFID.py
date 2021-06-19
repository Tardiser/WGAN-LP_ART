# This python file is used to calculate and save FID scores over different epochs.
# This code assumes that the mainTraining functions and classes are already defined.
# I have used 5000 images to calculate the statistics and repeated the FID calculation 8 times.
# Normally, it is recommended to use at least 25000 or 50000 images.

import sys  
sys.path.insert(0, '../input/fidpython/')

import fid  # FID code could be found in this repo: https://github.com/bioinf-jku/TTUR/blob/master/fid.py
def calculate_fid(images_real, images_fake):
  fid.create_inception_graph("../input/fidgraph/classify_image_graph_def.pb")  # load the graph into the current TF graph
  with tf.compat.v1.Session() as sess:
      sess.run(tf.compat.v1.global_variables_initializer())
      mu_gen, sigma_gen = fid.calculate_activation_statistics(images_fake, sess, batch_size=50)
      mu_real, sigma_real = fid.calculate_activation_statistics(images_real, sess, batch_size=50)

  fid_value = fid.calculate_frechet_distance(mu_gen, sigma_gen, mu_real, sigma_real)
  return fid_value


import shutil # It was required for loading models to have the same path, shutil is used to ensure that.
import json
fid_dict = {}
for i in range(200, 2000, 200):
    src = f'../input/savesversion66/{i}'
    dest = f'./savedModels/20210613_013128_model/{i}/'
    destination = shutil.copytree(src, dest)
    wgan.load_weights(dest)
    fid_list = []
    print(f"Calculating epoch {i}")
    for j in range(8):
        images_real, _ = load_real_data(images, 5000)
        images_real = images_real.astype(np.float32)
        
        random_latent_vectors = np.random.rand(5000, 100)
        images_fake = wgan.generator.predict(random_latent_vectors)

        print("Calculating FID...")
        fid_val = calculate_fid(images_real, images_fake)
        print(f'FID: {fid_val}')
        fid_list.append(fid_val)
    fid_dict[str(i)] = fid_list

file = open("./fidResults.json", "w")
json.dump(fid_dict, file)
file.close()
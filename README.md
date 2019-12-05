# SomethingSomethingVAE

Conv-VAE-Deconv network for music generation

**Goal**: G E N E R A E D   M U S A C

**Task**: Learn a model to predict upcoming notes given previous part of track

**Assumption**: Many model-generated pieces sound like a cacophony due to rapid changes, whereas [human music](https://www.youtube.com/watch?v=OB2ekdVqPnk) changes "smoothly" in some sense. Two consecutive parts of a track are similar due to some extent.

**Implication**: Information-saturated representations of two consecutive music blocks are very close to each other and may be represented as two samples from the same distribution. In this case rapid changes that actually take place may be viewed as a result of sampling process randomness. 

## General idea

* Transform MIDI-track into consecutive blocks of pianoroll-like images
* Extract features into a latent space vector via CNN
* Use the resampling part of VAE to get a new latent-space vector from the "same" distribution
* Deconvolve the vector back to pianoroll-like image
* Create MIDI-file out of the image

### Prerequisites

Other than ordinary scientific things you definitely have in your Conda environment by default?\
1. [music21](https://github.com/cuthbertLab/music21)
Just `pip install` it, the thing is available in the repo.

### Data

We are using [MAESTRO v2.0.0](https://magenta.tensorflow.org/datasets/maestro#v200) as our primary dataset. Download just the midi-files and proceed.

### Preprocessing

**WARNING** 
The preprocessing step takes HOURS to be completed due to presumably bad convertion algorithm.
If there is one thing to be `"Improved"(c)`, that's definitely that very phase.

1. Change `preprocessing.py` swapping `dataset_path` and `output_path` with directory your dataset is placed(that is, where `.csv`/`.json` files and MIDI-folders are placed) and where you want the image folders to be placed respectively
2. Run it
3. Wait
4. Wait more

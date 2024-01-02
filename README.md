# Submission for Deep Blue Hackathon

### Contents 
- The folder [Original_Images](Original_Images/) containing images from the original dataset.
- The folder [OutputImages](OutputImages/) containing images enhanced using <algo name here>.
- The folder [OutputImages_01](OutputImages_01/) containing images enhanced using <algo name here>.
- The folder [OutputImages_02](OutputImages_02/) containing images of OutputImages_01 with RGHS filter applied on them.
- The folder [CBNS_images](CBNS_images/) containing the images enhanced using the white balancing and fusion teachnique.


### Instructions 
- Make sure you are in the root directory
- To test code first of all install the requirements :
```
pip install -r requirements.txt
```
- Download the test images directory in the root
- The run code, simply run the command :
```
python main.py <$path to your images directory>
```
- The results will be saved in the [outputs](outputs/) directory

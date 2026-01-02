# Pelfit: AI-Powered Pelvic Tilt Detection

[![TensorFlow](https://img.shields.io/badge/TensorFlow-1.x-orange.svg)](https://tensorflow.org)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://python.org)
[![MedHacks 2017](https://img.shields.io/badge/MedHacks-2017-red.svg)](https://medhacks2017.devpost.com/)
🏆 **Wolfram Award Winner**

A web application that uses deep learning to detect pelvic tilt posture from side-profile photos. Built at MedHacks 2017.

> **Note**: Built on TensorFlow 1.x. The Heroku deployment is deprecated, but the model and code remain as a portfolio piece.

---

## The Problem

Pelvic tilt is a common posture issue that can lead to:
- Chronic lower back pain
- Hip and knee problems
- Neck and shoulder tension

Most people don't know they have it, and professional assessment typically requires a physical therapist visit.

## Our Solution

Upload a side-profile photo → Get an instant classification:

| Classification | Description |
|----------------|-------------|
| **Anterior Pelvic Tilt** | Pelvis tilted forward (most common) |
| **Posterior Pelvic Tilt** | Pelvis tilted backward |
| **Neutral** | Normal alignment |

---

## Technical Approach

### Transfer Learning from Inception

We used TensorFlow's [image retraining](https://www.tensorflow.org/hub/tutorials/image_retraining) approach:

1. **Base model**: Pre-trained Inception network (trained on ImageNet's 1M+ images)
2. **Transfer learning**: Retrained the final classification layer on our posture dataset
3. **Custom dataset**: ~60 labeled images across 3 categories
4. **Output**: 5.5MB frozen graph (`retrained_graph.pb`)

This approach allows training a custom classifier in minutes on a laptop, leveraging the visual feature representations already learned by Inception.

### Architecture

```
User uploads photo
       ↓
Flask web server (server.py)
       ↓
TensorFlow inference (label_image.py)
       ↓
Inception-based classifier (retrained_graph.pb)
       ↓
Classification result → displayed to user
```

---

## My Contribution

As noted on [Devpost](https://devpost.com/software/medhack-pelvic-tilt):
> "Worked on all of the Python (Flask/TensorFlow) and basic HTML for the project"

- Built the Flask web application (`server.py`)
- Integrated TensorFlow inference pipeline (`label_image.py`)
- Deployed to Heroku (now deprecated)
- Collaborated with 4 teammates on the 24-hour hackathon build

---

## Project Structure

```
├── server.py              # Flask web server
├── label_image.py         # TensorFlow inference
├── retrained_graph.pb     # Trained model (5.5MB)
├── retrained_labels.txt   # Class labels
├── templates/             # HTML templates
├── static/                # CSS and uploaded images
└── images/                # Training dataset
    ├── ant/               # Anterior tilt examples
    ├── post/              # Posterior tilt examples
    └── neutral/           # Neutral examples
```

---

## Links

- **Devpost**: [devpost.com/software/medhack-pelvic-tilt](https://devpost.com/software/medhack-pelvic-tilt)
- **Slides**: [Google Slides Presentation](https://docs.google.com/presentation/d/1uGiPUGKm7fNkHJHdGSvXNp-kbsz2CRTuczJ6UVhoGL0/edit?usp=sharing)

---

## References

- [TensorFlow Image Retraining Tutorial](https://www.tensorflow.org/hub/tutorials/image_retraining)
- Szegedy et al., ["Rethinking the Inception Architecture"](https://arxiv.org/abs/1512.00567) (CVPR 2016)

---

*MedHacks 2017 — Wolfram Award Winner*

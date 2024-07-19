from flask import Flask, render_template, request, jsonify
import os
import cv2
import face_recognition
import pickle
import numpy as np
import base64
import warnings

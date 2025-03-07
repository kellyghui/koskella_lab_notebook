[3/03/2025](#3032025)
- [Conclusions](#pfu-comparison) <br>

[3/10/2025](#3102025)

# 3/03/2025

### Phage Titer
- ~25.5 PFU on 10^-6 dil (90 uL plated)
- or should i use the phage titer from last week

## Plate Setup:
![IMG_3737](https://github.com/user-attachments/assets/e503f97c-cd5d-4c54-aa68-f6a406110b69)

## Results:

### Averaged Technical Replicates Per Biological Replicate
x axis is supposed to say Time (hr)
| Plot 1 | Plot 2 |
|--------|--------|
| ![Plot 1](https://github.com/user-attachments/assets/1974fa55-b4f2-4b6a-becf-68e661a8b0ab) | ![Plot 2](https://github.com/user-attachments/assets/19be0122-9e03-49b7-9c87-fa8e66fc7576) |

| Plot 3 | Plot 4 |
|--------|--------|
| ![Plot 3](https://github.com/user-attachments/assets/dee9b190-ac42-426b-8f5a-34e8a3ba444e) | ![Plot 4](https://github.com/user-attachments/assets/efff7e38-6f64-4b99-8135-4f4b25991587) |

### Averaged Technical Replicates Per Phage PFU

| 0 PFU | < 10 PFU | 10 PFU |
|--------|--------|--------|
| **AUC:** 95.03 | **AUC:** 79.05 | **AUC:** 78.26|
| **Standardized AUC:** 7.92 | **Standardized AUC:** 6.59 | **Standardized AUC:** 6.52|
| ![Plot 1a](https://github.com/user-attachments/assets/4e06f675-00a2-47a4-b9a1-e2a4c31ca2c7) <br> ![Plot 1b](https://github.com/user-attachments/assets/8c5b2d72-3528-465a-95a7-0f9eaf078e7c) | ![Plot 2a](https://github.com/user-attachments/assets/c3542019-7491-4cdc-b675-1cb687f42daa) <br> ![Plot 2b](https://github.com/user-attachments/assets/a1906915-3c30-42f7-8aff-c0b8a6d76056) | ![Plot 3a](https://github.com/user-attachments/assets/a24f4282-7072-4296-8433-c44ec99893d5) <br> ![Plot 3b](https://github.com/user-attachments/assets/44c68a87-f789-41d8-8e0b-fd41ca6318a4) |

| 10^2 PFU | 10^3 PFU | 10^4 PFU |
|--------|--------|--------|
| **AUC:** 73.17 | **AUC:** 73.48 | **AUC:** 69.52|
| **Standardized AUC:** 6.10 | **Standardized AUC:** 6.12 | **Standardized AUC:** 5.79|
| ![Plot 4a](https://github.com/user-attachments/assets/84b85f65-f1c2-46c2-8e8e-da31608504df) <br> ![Plot 4b](https://github.com/user-attachments/assets/285213c5-47c2-4b9d-ba61-70280652add6) | ![Plot 5a](https://github.com/user-attachments/assets/9d63c93f-bb0e-4c58-bcad-7285d4263fae) <br> ![Plot 5b](https://github.com/user-attachments/assets/81d05b2c-5c50-41f2-afc8-6870d2359a02) | ![Plot 6a](https://github.com/user-attachments/assets/92a0afe1-0c1a-4e5b-b8c5-9ff7ec787c0e) <br> ![Plot 6b](https://github.com/user-attachments/assets/9abdea7c-9b68-45fe-aa94-89fd041cbcc4) |

| 10^5 PFU | 10^6 PFU | Empty |
|--------|--------|-------|
| **AUC:** 61.97 | **AUC:** 61.78 |
| **Standardized AUC:** 5.16 | **Standardized AUC:** 5.15 | 
| ![Plot 7a](https://github.com/user-attachments/assets/f2bc1ff3-8797-4301-85e2-a6e684effb6f) <br> ![Plot 7b](https://github.com/user-attachments/assets/58ba8201-5ad2-4c36-945f-48c51daeb83f) | ![Plot 8a](https://github.com/user-attachments/assets/5be0186e-a97f-4715-aa4a-3d28c5fcfebd) <br> ![Plot 8b](https://github.com/user-attachments/assets/d83522f3-f3ed-40ca-9fa9-261a2fc5ffa2) | ![image](https://github.com/user-attachments/assets/926e54d2-29ae-4b07-82c1-2cef1fde6812) |

### Technical Replicates Averaged at 12 hour mark
![Plot 1](https://github.com/user-attachments/assets/bdbc2c0d-d37d-474c-9e24-222e08a86302)



<a name="pfu-comparison"></a>
### Compare 10^4 PFU for combined biological replicates (from RBG: 10/03/24 + 10/31/24) & technical reps (from RBG_Ver2 3/03/25)
Variance Test (using np.var):
- Variance of technical replicates: 0.0018
- Variance of biological replicates: 0.0032
- Technical replicates have less variance <br>

Levene's Test (scipy.stats): Compares variance of two distributions, is robust to non-normal distributions.
- Levene’s test statistic: 241.81573066018305, p-value: 2.266995930056248e-53
- Reject null hypothesis: Variances are significantly different.

# 3/10/2025

### Phage Titer 
- ..

## Plate Setup


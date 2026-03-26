# AI Resume Analyzer - Deployment Guide

## Live Deployment
Your app is deployed at: **https://ai-resume-analyzer.onrender.com**

## Setup Cloud Database (PlanetScale)

### Step 1: Create PlanetScale Account
1. Go to https://planetscale.com
2. Click "Sign up" (use GitHub or email)
3. Create account

### Step 2: Create Database
1. Click "Create" → "New database"
2. Name: `resume`
3. Region: Choose closest to you
4. Click "Create database"

### Step 3: Get Connection String
1. In your database, click "Connect"
2. Select "MySQL" (if prompted)
3. Copy the connection string (looks like):
   ```
   mysql://xxxx:pscale_xxxx@aws.connect.psdb.cloud/resume?sslaccept=strict
   ```

### Step 4: Add to Render
1. Go to https://dashboard.render.com
2. Click "ai-resume-analyzer" service
3. Click "Environment" tab
4. Click "Add Environment Variable"
5. Fill in:
   - **KEY:** `DATABASE_URL`
   - **VALUE:** (paste your connection string from Step 3)
6. Click "Save"
7. Render auto-redeploys (watch logs)

### Step 5: Done!
Your app now has:
✅ Cloud database (PlanetScale - free)
✅ Auto-deployment (Render - free)
✅ Resume analysis working
✅ User data saving

## Features
- Upload & analyze resumes
- Get skill recommendations
- Course suggestions
- Admin dashboard (User/Rohith@91)
- User feedback system

## Support
If issues occur:
1. Check Render logs
2. Check PlanetScale connection
3. Verify DATABASE_URL is correct

---
Built with ❤️ by Rohith

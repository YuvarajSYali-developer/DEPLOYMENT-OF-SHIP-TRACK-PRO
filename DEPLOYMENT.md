# 🚀 Free Deployment Guide

This guide will help you deploy your ShipTrack Pro application using free hosting services.

## 📋 Prerequisites

1. **GitHub Account** - Create one at [github.com](https://github.com)
2. **Git installed** - Download from [git-scm.com](https://git-scm.com)

## 🎯 Deployment Strategy

- **Frontend**: Vercel (Free tier)
- **Backend**: Railway (Free tier)
- **Database**: Railway PostgreSQL (Free tier)

## 📦 Step 1: Push to GitHub

1. **Initialize Git repository:**
```bash
git init
git add .
git commit -m "Initial commit - ShipTrack Pro"
```

2. **Create GitHub repository:**
   - Go to [github.com](https://github.com) and create a new repository
   - Name it: `shiptrack-pro` or similar
   - Don't initialize with README (we already have files)

3. **Push to GitHub:**
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

## 🚂 Step 2: Deploy Backend on Railway

1. **Sign up for Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign up with your GitHub account

2. **Create new project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure environment variables:**
   - In Railway dashboard, go to your project
   - Click on "Variables" tab
   - Add these variables:
     ```
     ENVIRONMENT=production
     FRONTEND_URL=https://your-app-name.vercel.app
     ```

4. **Railway will automatically:**
   - Detect it's a Python app
   - Install dependencies from requirements.txt
   - Use the railway.toml configuration
   - Deploy your backend

5. **Get your backend URL:**
   - After deployment, Railway will provide a URL like:
   - `https://your-app-name.railway.app`

## 🌐 Step 3: Deploy Frontend on Vercel

1. **Sign up for Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Sign up with your GitHub account

2. **Import project:**
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will detect it's a Vue.js app

3. **Configure build settings:**
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

4. **Set environment variables:**
   - In Vercel dashboard, go to Settings > Environment Variables
   - Add: `VITE_API_URL` = `https://your-backend-url.railway.app`

5. **Deploy:**
   - Click "Deploy"
   - Vercel will build and deploy your frontend

## 🔄 Step 4: Update CORS Settings

After getting your Vercel URL:

1. **Update Railway environment variables:**
   - Go to Railway dashboard
   - Update `FRONTEND_URL` with your actual Vercel URL
   - Example: `https://shiptrack-pro.vercel.app`

2. **Redeploy backend:**
   - Railway will automatically redeploy with new settings

## ✅ Step 5: Test Your Deployment

1. **Visit your frontend URL** (from Vercel)
2. **Try logging in** with test credentials:
   - Admin: `admin` / `admin123`
   - Manager: `manager` / `manager123`
3. **Check API documentation** at your Railway URL + `/docs`

## 🎉 You're Live!

Your application is now deployed and accessible worldwide!

- **Frontend**: `https://your-app.vercel.app`
- **Backend**: `https://your-app.railway.app`
- **API Docs**: `https://your-app.railway.app/docs`

## 💡 Free Tier Limits

- **Vercel**: 100GB bandwidth/month, unlimited projects
- **Railway**: $5 credit/month (enough for small apps)
- **Database**: Railway PostgreSQL included in free tier

## 🔧 Troubleshooting

**CORS Errors:**
- Make sure FRONTEND_URL is set correctly in Railway
- Check that both URLs use HTTPS

**Build Failures:**
- Check build logs in respective dashboards
- Ensure all dependencies are in package.json/requirements.txt

**Database Issues:**
- Currently using SQLite (file-based)
- For production, consider migrating to PostgreSQL

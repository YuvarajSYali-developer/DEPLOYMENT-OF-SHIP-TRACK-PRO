#!/usr/bin/env python3
"""
Migration script to move from SQLite to PostgreSQL for production
Run this after setting up PostgreSQL database on Railway
"""

import os
import sqlite3
from sqlmodel import create_engine, Session, SQLModel
from working_server import *  # Import all models

def migrate_sqlite_to_postgres():
    """Migrate data from SQLite to PostgreSQL"""
    
    # PostgreSQL connection (from environment variable)
    postgres_url = os.environ.get("DATABASE_URL")
    if not postgres_url:
        print("❌ DATABASE_URL environment variable not set")
        print("Please set it to your Railway PostgreSQL URL")
        return
    
    # Fix postgres:// to postgresql:// if needed (Railway uses postgres://)
    if postgres_url.startswith("postgres://"):
        postgres_url = postgres_url.replace("postgres://", "postgresql://", 1)
    
    print(f"🔄 Migrating from SQLite to PostgreSQL...")
    print(f"📊 Target database: {postgres_url.split('@')[1] if '@' in postgres_url else 'PostgreSQL'}")
    
    # Create PostgreSQL engine
    pg_engine = create_engine(postgres_url, echo=True)
    
    # Create all tables in PostgreSQL
    SQLModel.metadata.create_all(pg_engine)
    print("✅ Created tables in PostgreSQL")
    
    # Connect to SQLite
    sqlite_path = "./indian_shipment.db"
    if not os.path.exists(sqlite_path):
        print(f"❌ SQLite database not found at {sqlite_path}")
        return
    
    sqlite_engine = create_engine(f"sqlite:///{sqlite_path}")
    
    # Migrate data
    with Session(sqlite_engine) as sqlite_session, Session(pg_engine) as pg_session:
        # Migrate Users
        users = sqlite_session.exec(select(User)).all()
        for user in users:
            pg_session.add(user)
        print(f"✅ Migrated {len(users)} users")
        
        # Migrate Customers
        customers = sqlite_session.exec(select(Customer)).all()
        for customer in customers:
            pg_session.add(customer)
        print(f"✅ Migrated {len(customers)} customers")
        
        # Migrate Shipments
        shipments = sqlite_session.exec(select(Shipment)).all()
        for shipment in shipments:
            pg_session.add(shipment)
        print(f"✅ Migrated {len(shipments)} shipments")
        
        # Commit all changes
        pg_session.commit()
    
    print("🎉 Migration completed successfully!")
    print("💡 Update your working_server.py to use DATABASE_URL environment variable")

if __name__ == "__main__":
    migrate_sqlite_to_postgres()

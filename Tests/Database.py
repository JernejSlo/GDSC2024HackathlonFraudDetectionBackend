import os
from supabase import create_client, Client

url: str = "https://xjrqindnljihkclzhzgm.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhqcnFpbmRubGppaGtjbHpoemdtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTQ4NDI2NTIsImV4cCI6MjAzMDQxODY1Mn0.XAGz0zRBoqo4MCoew6678AX_ej-8VWUPUxL5AGkJMbA"
supabase: Client = create_client(url, key)


response = supabase.table('UserInfo').select("*").execute()
print(response.data)
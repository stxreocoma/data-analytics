import pandas as pd

def Open(filepath):
    try:
        return pd.read_excel(filepath)
    except FileNotFoundError:
        print(f"error: file {filepath} not found")
        return None
    except Exception:
        print(f"error while open file: {Exception}")
        return None

def check(cols=None):
    def decorator(func):
        def wrapper(df, *args, **kwargs):
            if df is None or df.empty:
                print("dataset missing or empty")
                return
            
            if cols:
                missing = [col for col in cols if col not in df.columns]
                if missing:
                    print(f"columns not found: {', '.join(missing)}")
                    return
                
            return func(df, *args, **kwargs)
        
        return wrapper
    
    return decorator
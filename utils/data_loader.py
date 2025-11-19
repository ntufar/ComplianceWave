import pandas as pd

def load_data(filepath):
    """Loads the mandate data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        return pd.DataFrame()

def filter_data(df, year, scope, region):
    """Filters the dataframe based on year, scope, and region."""
    if df.empty:
        return df
    
    # Filter by Year (Logic: Show status if mandate year <= selected year)
    # For simplicity in this MVP, we assume the status in the CSV is the "final" status
    # and we might want to show "No Mandate" if the current year < mandate year.
    # However, the PRD implies a static list. Let's stick to the simple view first,
    # but maybe add a "Effective Status" column logic if needed.
    # For now, we just return the data. The visualization will handle the "time" aspect 
    # by potentially filtering or coloring based on the year comparison.
    
    # Actually, for the map to "evolve", we need to determine the status AT the selected year.
    # Let's add a derived column 'Current_Status' for the visualization.
    
    def get_status_at_year(row, selected_year):
        mandate_year = row['Year']
        if selected_year >= mandate_year:
            return row['Status_B2B'] # Defaulting to B2B status for the main map color
        else:
            return "No Mandate" # Or "Upcoming" if close? PRD says "Orange: Upcoming".
            # Let's keep it simple: If selected_year < mandate_year, it's "Upcoming" or "No Mandate"
            # depending on how far out.
            # PRD: "Orange: Upcoming Mandate (Announced but not live)"
            # "Grey: No Mandate"
            
    # We will handle this logic in the main app or here. 
    # Let's just return the full DF here and let the app handle display logic 
    # to keep data loader pure.
    
    # Region filtering (Placeholder as we don't have Region column in CSV yet, 
    # but PRD mentioned it. We can map it or ignore for MVP step 1).
    # if region != "Global":
    #     df = df[df['Region'] == region]
        
    return df

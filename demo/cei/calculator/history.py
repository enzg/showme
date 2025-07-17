"""
History management for calculator operations.
Stores calculation history and provides methods to retrieve and manage it.
"""
from typing import List, Optional, Dict
from datetime import datetime
import json


class HistoryEntry:
    """Represents a single calculation in history."""
    
    def __init__(self, expression: str, result: float, timestamp: Optional[datetime] = None):
        """
        Initialize a history entry.
        
        Args:
            expression: The mathematical expression
            result: The calculated result
            timestamp: When the calculation was performed (defaults to now)
        """
        self.expression = expression
        self.result = result
        self.timestamp = timestamp or datetime.now()
    
    def __repr__(self):
        return f"HistoryEntry('{self.expression}', {self.result}, {self.timestamp})"
    
    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            'expression': self.expression,
            'result': self.result,
            'timestamp': self.timestamp.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'HistoryEntry':
        """Create HistoryEntry from dictionary."""
        return cls(
            expression=data['expression'],
            result=data['result'],
            timestamp=datetime.fromisoformat(data['timestamp'])
        )
    
    def format_display(self) -> str:
        """Format entry for display."""
        # Format result to remove unnecessary decimal places
        result_str = f"{self.result:.10g}"
        return f"{self.expression} = {result_str}"


class HistoryManager:
    """
    Manages calculation history.
    Stores history in memory with optional persistence to file.
    """
    
    def __init__(self, max_entries: int = 100):
        """
        Initialize history manager.
        
        Args:
            max_entries: Maximum number of entries to keep in history
        """
        self.max_entries = max_entries
        self._history: List[HistoryEntry] = []
    
    def add_entry(self, expression: str, result: float) -> None:
        """
        Add a new calculation to history.
        
        Args:
            expression: The mathematical expression
            result: The calculated result
        """
        entry = HistoryEntry(expression, result)
        self._history.append(entry)
        
        # Maintain max entries limit
        if len(self._history) > self.max_entries:
            self._history = self._history[-self.max_entries:]
    
    def get_history(self, limit: Optional[int] = None) -> List[HistoryEntry]:
        """
        Retrieve calculation history.
        
        Args:
            limit: Maximum number of entries to return (None for all)
            
        Returns:
            List of history entries, most recent last
        """
        if limit is None:
            return self._history.copy()
        
        # Return the last 'limit' entries
        return self._history[-limit:] if limit > 0 else []
    
    def get_recent(self, count: int = 10) -> List[HistoryEntry]:
        """
        Get the most recent calculations.
        
        Args:
            count: Number of recent entries to return
            
        Returns:
            List of recent history entries
        """
        return self.get_history(limit=count)
    
    def clear_history(self) -> None:
        """Clear all history entries."""
        self._history.clear()
    
    def is_empty(self) -> bool:
        """Check if history is empty."""
        return len(self._history) == 0
    
    def size(self) -> int:
        """Get the number of entries in history."""
        return len(self._history)
    
    def search(self, query: str) -> List[HistoryEntry]:
        """
        Search history for entries containing the query.
        
        Args:
            query: Search string
            
        Returns:
            List of matching history entries
        """
        query = query.lower()
        return [
            entry for entry in self._history
            if query in entry.expression.lower() or 
               query in str(entry.result).lower()
        ]
    
    def get_by_index(self, index: int) -> Optional[HistoryEntry]:
        """
        Get history entry by index.
        
        Args:
            index: Index in history (negative indices supported)
            
        Returns:
            HistoryEntry or None if index out of range
        """
        try:
            return self._history[index]
        except IndexError:
            return None
    
    def save_to_file(self, filepath: str) -> None:
        """
        Save history to JSON file.
        
        Args:
            filepath: Path to save file
        """
        data = {
            'max_entries': self.max_entries,
            'history': [entry.to_dict() for entry in self._history]
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filepath: str) -> None:
        """
        Load history from JSON file.
        
        Args:
            filepath: Path to load file
            
        Raises:
            FileNotFoundError: If file doesn't exist
            json.JSONDecodeError: If file is not valid JSON
        """
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        self.max_entries = data.get('max_entries', self.max_entries)
        self._history = [
            HistoryEntry.from_dict(entry_data) 
            for entry_data in data.get('history', [])
        ]
    
    def format_history_display(self, limit: Optional[int] = None) -> str:
        """
        Format history for text display.
        
        Args:
            limit: Maximum number of entries to display
            
        Returns:
            Formatted string of history entries
        """
        entries = self.get_history(limit)
        if not entries:
            return "No calculation history"
        
        lines = ["Calculation History:", "-" * 40]
        for i, entry in enumerate(entries, 1):
            time_str = entry.timestamp.strftime("%H:%M:%S")
            lines.append(f"{i}. [{time_str}] {entry.format_display()}")
        
        return "\n".join(lines)
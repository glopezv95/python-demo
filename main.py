from populate import compute

def main():
    
    print('-----------------------')
    compute(name = 'people')
    compute(name = 'ccaa')
    compute(name = 'provinces')
    compute(name = 'departments')
    compute(name = 'projects')
    
    print(f'Database generated successfully.')
    print()
    
if __name__ == '__main__':
    
    main()
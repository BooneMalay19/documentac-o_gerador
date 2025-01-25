from git import Repo

def clone_repository(repo_url, clone_dir):
  
    try:
        Repo.clone_from(repo_url, clone_dir)
        return clone_dir
    except Exception as e:
        print(f"Erro ao clonar o repositório: {e}")
        return None